#!/bin/bash
set -e

echo "🚀 Embedding Cache Example - Quick Start"
echo "========================================"
echo ""

# Check if Redis is running
if ! docker-compose ps | grep -q "redis.*Up"; then
    echo "📦 Starting Redis..."
    docker-compose up -d
    echo "⏳ Waiting for Redis to be ready..."
    sleep 3

    # Wait for Redis health check
    timeout=30
    elapsed=0
    while [ $elapsed -lt $timeout ]; do
        if docker exec embedding-cache-redis redis-cli ping 2>/dev/null | grep -q "PONG"; then
            echo "✓ Redis is ready"
            break
        fi
        sleep 1
        elapsed=$((elapsed + 1))
    done

    if [ $elapsed -ge $timeout ]; then
        echo "❌ Redis failed to start within ${timeout}s"
        exit 1
    fi
else
    echo "✓ Redis is already running"
fi

echo ""
echo "🏃 Running demo..."
echo ""

cargo run --release

echo ""
echo "📊 Redis Stats:"
docker exec embedding-cache-redis redis-cli INFO stats | grep -E "keyspace_hits|keyspace_misses|total_commands_processed"

echo ""
echo "💾 Redis Memory:"
docker exec embedding-cache-redis redis-cli INFO memory | grep -E "used_memory_human|maxmemory_human"

echo ""
echo "🔑 Cached Keys:"
docker exec embedding-cache-redis redis-cli DBSIZE

echo ""
echo "✨ Demo complete!"
echo ""
echo "To stop Redis: docker-compose down"
echo "To clean Redis data: docker-compose down -v"
