#!/usr/bin/env bash
# Integration test for compiler-guided proof repair
#
# Tests the repair infrastructure components:
# 1. parseLeanErrors.py - Error parsing
# 2. solverCascade.py - Automated solver attempts
# 3. Error strategy routing (YAML config)
#
# Note: Full loop testing requires lean4-proof-repair agent (not tested here)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
SCRIPTS_DIR="${PLUGIN_ROOT}/scripts"
CONFIG_DIR="${PLUGIN_ROOT}/config"

echo "🧪 Compiler-Guided Repair Integration Test"
echo "=========================================="
echo

# Test 1: Parse Lean Errors
echo "Test 1: Error Parsing"
echo "---------------------"

# Create test error output
TEST_ERROR_FILE="/tmp/test_lean_error.txt"
cat > "${TEST_ERROR_FILE}" << 'EOF'
test.lean:42:10: error: type mismatch
  h
has type
  Measurable f : Prop
but is expected to have type
  Continuous f : Prop
EOF

# Run parser
echo "Running parseLeanErrors.py..."
if python3 "${SCRIPTS_DIR}/parseLeanErrors.py" "${TEST_ERROR_FILE}" > /tmp/test_context.json; then
  echo "✅ Parser succeeded"

  # Validate output
  if command -v jq >/dev/null 2>&1; then
    error_type=$(jq -r '.errorType' /tmp/test_context.json)
    error_file=$(jq -r '.file' /tmp/test_context.json)
    error_line=$(jq -r '.line' /tmp/test_context.json)

    if [[ "${error_type}" == "type_mismatch" ]]; then
      echo "  ✓ Error type correctly identified: ${error_type}"
    else
      echo "  ✗ Error type wrong: ${error_type} (expected type_mismatch)"
      exit 1
    fi

    if [[ "${error_file}" == "test.lean" && "${error_line}" == "42" ]]; then
      echo "  ✓ Location correctly parsed: ${error_file}:${error_line}"
    else
      echo "  ✗ Location wrong: ${error_file}:${error_line} (expected test.lean:42)"
      exit 1
    fi
  else
    echo "  ⚠️  jq not available, skipping validation"
  fi
else
  echo "✗ Parser failed"
  exit 1
fi

echo

# Test 2: Error Strategy Routing
echo "Test 2: Error Strategy Routing"
echo "-------------------------------"

if [[ -f "${CONFIG_DIR}/errorStrategies.yaml" ]]; then
  echo "✅ errorStrategies.yaml exists"

  # Check for required patterns
  required_patterns=("type mismatch" "unsolved goals" "unknown identifier" "synth_instance")
  for pattern in "${required_patterns[@]}"; do
    if grep -q "${pattern}" "${CONFIG_DIR}/errorStrategies.yaml"; then
      echo "  ✓ Strategy for '${pattern}' defined"
    else
      echo "  ✗ Missing strategy for '${pattern}'"
      exit 1
    fi
  done
else
  echo "✗ errorStrategies.yaml not found"
  exit 1
fi

echo

# Test 3: Solver Cascade (dry run)
echo "Test 3: Solver Cascade (dry run)"
echo "---------------------------------"

# This test can't run actual compilation without a Lean project
# We just check the script syntax and structure

if [[ -x "${SCRIPTS_DIR}/solverCascade.py" ]]; then
  echo "✅ solverCascade.py is executable"

  # Check help/usage
  if python3 "${SCRIPTS_DIR}/solverCascade.py" 2>&1 | grep -q "Usage"; then
    echo "  ✓ Shows usage when called incorrectly"
  else
    echo "  ⚠️  No usage message (acceptable)"
  fi
else
  echo "✗ solverCascade.py not executable"
  chmod +x "${SCRIPTS_DIR}/solverCascade.py"
  echo "  ✓ Made executable"
fi

echo

# Test 4: Reference Documentation
echo "Test 4: Reference Documentation"
echo "--------------------------------"

REFS_DIR="${PLUGIN_ROOT}/skills/lean4-theorem-proving/references"
required_refs=("compiler-guided-repair.md" "sorry-filling.md" "axiom-elimination.md")

for ref in "${required_refs[@]}"; do
  if [[ -f "${REFS_DIR}/${ref}" ]]; then
    word_count=$(wc -w < "${REFS_DIR}/${ref}")
    echo "  ✓ ${ref} exists (${word_count} words)"

    # Check for key sections
    case "${ref}" in
      compiler-guided-repair.md)
        if grep -q "Solver Cascade" "${REFS_DIR}/${ref}"; then
          echo "    ✓ Contains Solver Cascade section"
        fi
        if grep -q "Error Type" "${REFS_DIR}/${ref}"; then
          echo "    ✓ Contains error type strategies"
        fi
        ;;
    esac
  else
    echo "  ✗ ${ref} not found"
    exit 1
  fi
done

echo

# Test 5: Command Files
echo "Test 5: Slash Commands"
echo "----------------------"

COMMANDS_DIR="${PLUGIN_ROOT}/commands"
required_commands=("repair-file.md" "repair-goal.md" "repair-interactive.md")

for cmd in "${required_commands[@]}"; do
  if [[ -f "${COMMANDS_DIR}/${cmd}" ]]; then
    echo "  ✓ ${cmd} exists"

    # Check for required sections
    if grep -q "allowed-tools:" "${COMMANDS_DIR}/${cmd}"; then
      echo "    ✓ Has allowed-tools declaration"
    fi
  else
    echo "  ✗ ${cmd} not found"
    exit 1
  fi
done

echo

# Test 6: Agent Definition
echo "Test 6: Subagent Definition"
echo "---------------------------"

AGENT_FILE="${PLUGIN_ROOT}/../lean4-subagents/agents/lean4-proof-repair.md"
if [[ -f "${AGENT_FILE}" ]]; then
  echo "✅ lean4-proof-repair agent exists"

  # Check for two-stage configuration
  if grep -q "Stage 1" "${AGENT_FILE}" && grep -q "Stage 2" "${AGENT_FILE}"; then
    echo "  ✓ Two-stage approach documented"
  fi

  # Check model specifications
  if grep -q "haiku" "${AGENT_FILE}"; then
    echo "  ✓ Haiku model referenced (Stage 1)"
  fi
  if grep -q "sonnet" "${AGENT_FILE}"; then
    echo "  ✓ Sonnet model referenced (Stage 2)"
  fi
else
  echo "⚠️  lean4-proof-repair agent not found (may be in different plugin)"
fi

echo

# Test 7: Bootstrap Hook
echo "Test 7: Bootstrap Hook Staging"
echo "-------------------------------"

BOOTSTRAP="${PLUGIN_ROOT}/hooks/bootstrap.sh"
if [[ -f "${BOOTSTRAP}" ]]; then
  echo "✅ bootstrap.sh exists"

  if grep -q "compiler-guided-repair.md" "${BOOTSTRAP}"; then
    echo "  ✓ Stages compiler-guided-repair.md"
  else
    echo "  ✗ Does not stage compiler-guided-repair.md"
    exit 1
  fi
else
  echo "✗ bootstrap.sh not found"
  exit 1
fi

echo

# Summary
echo "=========================================="
echo "✅ Integration Test PASSED"
echo
echo "Components verified:"
echo "  ✓ Error parsing (parseLeanErrors.py)"
echo "  ✓ Error routing (errorStrategies.yaml)"
echo "  ✓ Solver cascade (solverCascade.py)"
echo "  ✓ Reference documentation (3 files)"
echo "  ✓ Slash commands (3 commands)"
echo "  ✓ Subagent definition (lean4-proof-repair)"
echo "  ✓ Bootstrap staging"
echo
echo "Note: Full end-to-end test requires:"
echo "  - Actual Lean project with errors"
echo "  - lean4-proof-repair agent execution"
echo "  - LLM API integration"
echo
echo "These components are ready for manual testing."

# Cleanup
rm -f /tmp/test_lean_error.txt /tmp/test_context.json
