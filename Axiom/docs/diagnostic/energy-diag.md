---
name: energy-diag
description: Symptom-based energy troubleshooting — decision trees for 'app at top of battery settings', 'phone gets hot', 'background drain', 'high cellular usage', with time-cost analysis for each diagnosis path
version: 1.0.0
---

# Energy Diagnostics

Symptom-based troubleshooting for energy issues. Start with your symptom, follow the decision tree, get the fix.

**Related skills**: `energy` (patterns, checklists), `energy-ref` (API reference)

## Symptom 1: App at Top of Battery Settings

Users or you notice your app consuming significant battery.

### Diagnosis Decision Tree

```
App at top of Battery Settings?
│
├─ Step 1: Run Power Profiler (15 min)
│  ├─ CPU Power Impact high?
│  │  ├─ Continuous? → Timer leak or polling loop
│  │  │  └─ Fix: Check timers, add tolerance, convert to push
│  │  └─ Spikes during actions? → Eager loading or repeated parsing
│  │     └─ Fix: Use LazyVStack, cache parsed data
│  │
│  ├─ Network Power Impact high?
│  │  ├─ Many small requests? → Batching issue
│  │  │  └─ Fix: Batch requests, use discretionary URLSession
│  │  └─ Regular intervals? → Polling pattern
│  │     └─ Fix: Convert to push notifications
│  │
│  ├─ GPU Power Impact high?
│  │  ├─ Animations? → Running when not visible
│  │  │  └─ Fix: Stop in viewWillDisappear
│  │  └─ Blur effects? → Over dynamic content
│  │     └─ Fix: Remove or use static backgrounds
│  │
│  └─ Display Power Impact high?
│     └─ Light backgrounds on OLED?
│        └─ Fix: Implement Dark Mode (up to 70% savings)
│
└─ Step 2: Check background section in Battery Settings
   ├─ High background time?
   │  ├─ Location icon visible? → Continuous location
   │  │  └─ Fix: Switch to significant-change monitoring
   │  ├─ Audio active? → Session not deactivated
   │  │  └─ Fix: Deactivate audio session when not playing
   │  └─ BGTasks running long? → Not completing promptly
   │     └─ Fix: Call setTaskCompleted sooner
   │
   └─ Background time appropriate?
      └─ Issue is in foreground usage → Focus on CPU/GPU fixes above
```

### Time-Cost Analysis

| Approach | Time | Accuracy |
|----------|------|----------|
| Run Power Profiler, identify subsystem | 15-20 min | High |
| Guess and optimize random areas | 4+ hours | Low |
| Read all code looking for issues | 2+ hours | Medium |

**Recommendation**: Always use Power Profiler first. It costs 15 minutes but guarantees you optimize the right subsystem.

## Symptom 2: Device Gets Hot

Device temperature increases noticeably during app use.

### Diagnosis Decision Tree

```
Device gets hot during app use?
│
├─ Hot during specific action?
│  │
│  ├─ During video/camera use?
│  │  ├─ Video encoding? → Expected, but check efficiency
│  │  │  └─ Fix: Use hardware encoding, reduce resolution if possible
│  │  └─ Camera active unnecessarily? → Not releasing session
│  │     └─ Fix: Call stopRunning() when done
│  │
│  ├─ During scroll/animation?
│  │  ├─ GPU-intensive effects? → Blur, shadows, many layers
│  │  │  └─ Fix: Reduce effects, cache rendered content
│  │  └─ High frame rate? → Unnecessary 120fps
│  │     └─ Fix: Use CADisplayLink preferredFrameRateRange
│  │
│  └─ During data processing?
│     ├─ JSON parsing? → Repeated or large payloads
│     │  └─ Fix: Cache parsed results, paginate
│     └─ Image processing? → Synchronous on main thread
│        └─ Fix: Move to background, cache results
│
├─ Hot during normal use (no specific action)?
│  │
│  ├─ Run Power Profiler to identify:
│  │  ├─ CPU high continuously → Timer, polling, tight loop
│  │  ├─ GPU high continuously → Animation leak
│  │  └─ Network high continuously → Polling pattern
│  │
│  └─ Check for infinite loops or runaway recursion
│     └─ Use Time Profiler in Instruments
│
└─ Hot only in background?
   ├─ Location updates continuous? → High accuracy or no stop
   │  └─ Fix: Reduce accuracy, stop when done
   ├─ Audio session active? → Hardware kept powered
   │  └─ Fix: Deactivate when not playing
   └─ BGTask running too long? → System may throttle
      └─ Fix: Complete tasks faster, use requiresExternalPower
```

### Time-Cost Analysis

| Approach | Time | Outcome |
|----------|------|---------|
| Power Profiler + Time Profiler | 20-30 min | Identifies exact cause |
| Check code for obvious issues | 1-2 hours | May miss non-obvious causes |
| Wait for user complaints | N/A | Reputation damage |

## Symptom 3: Background Battery Drain

App drains battery even when user isn't actively using it.

### Diagnosis Decision Tree

```
High background battery usage?
│
├─ Step 1: Check Info.plist background modes
│  │
│  ├─ "location" enabled?
│  │  ├─ Actually need background location?
│  │  │  ├─ YES → Use significant-change, lowest accuracy
│  │  │  └─ NO → Remove background mode, use when-in-use only
│  │  └─ Check: Is stopUpdatingLocation called?
│  │
│  ├─ "audio" enabled?
│  │  ├─ Audio playing? → Expected
│  │  ├─ Audio NOT playing? → Session still active
│  │  │  └─ Fix: Deactivate session, use autoShutdownEnabled
│  │  └─ Playing silent audio? → Anti-pattern for keeping app alive
│  │     └─ Fix: Use proper background API (BGTask)
│  │
│  ├─ "fetch" enabled?
│  │  └─ Check: Is earliestBeginDate reasonable? (not too frequent)
│  │
│  └─ "remote-notification" enabled?
│     └─ Expected for push updates, check didReceiveRemoteNotification efficiency
│
├─ Step 2: Check BGTaskScheduler usage
│  │
│  ├─ BGAppRefreshTask scheduled too frequently?
│  │  └─ Fix: Increase earliestBeginDate interval
│  │
│  ├─ BGProcessingTask not using requiresExternalPower?
│  │  └─ Fix: Add requiresExternalPower = true for non-urgent work
│  │
│  └─ Tasks not completing? (setTaskCompleted not called)
│     └─ Fix: Always call setTaskCompleted, implement expirationHandler
│
└─ Step 3: Check beginBackgroundTask usage
   │
   ├─ endBackgroundTask called promptly?
   │  └─ Fix: Call immediately after work completes, not at expiration
   │
   └─ Multiple overlapping background tasks?
      └─ Fix: Track task IDs, ensure each is ended
```

### Common Background Drain Patterns

| Pattern | Power Profiler Signature | Fix |
|---------|--------------------------|-----|
| Continuous location | CPU lane + location icon | significant-change |
| Audio session leak | CPU lane steady | setActive(false) |
| Timer not invalidated | CPU spikes at intervals | invalidate in background |
| Polling from background | Network lane at intervals | Push notifications |
| BGTask too long | CPU sustained | Faster completion |

### Time-Cost Analysis

| Approach | Time | Outcome |
|----------|------|---------|
| Check Info.plist + BGTask code | 30 min | Finds common issues |
| On-device Power Profiler trace | 1-2 hours (real usage) | Captures real behavior |
| User-collected trace | Variable | Best for unreproducible issues |

## Symptom 4: High Energy Only on Cellular

Battery drains faster on cellular than WiFi.

### Diagnosis Decision Tree

```
High battery drain on cellular only?
│
├─ Expected: Cellular radio uses more power than WiFi
│  └─ But: Excessive drain indicates optimization opportunity
│
├─ Check URLSession configuration
│  │
│  ├─ allowsExpensiveNetworkAccess = true (default)?
│  │  └─ Fix: Set to false for non-urgent requests
│  │
│  ├─ isDiscretionary = false (default)?
│  │  └─ Fix: Set to true for background downloads
│  │
│  └─ waitsForConnectivity = false (default)?
│     └─ Fix: Set to true to avoid failed connection retries
│
├─ Check request patterns
│  │
│  ├─ Many small requests? → High connection overhead
│  │  └─ Fix: Batch into fewer larger requests
│  │
│  ├─ Polling? → Radio stays active
│  │  └─ Fix: Push notifications
│  │
│  └─ Large downloads in foreground? → Could wait for WiFi
│     └─ Fix: Use background URLSession with discretionary
│
└─ Check Low Data Mode handling
   ├─ Respecting allowsConstrainedNetworkAccess?
   │  └─ Fix: Set to false for non-essential requests
   │
   └─ Checking ProcessInfo.processInfo.isLowDataModeEnabled?
      └─ Fix: Reduce payload sizes, defer non-essential transfers
```

### Time-Cost Analysis

| Approach | Time | Outcome |
|----------|------|---------|
| Review URLSession configs | 15 min | Quick wins |
| Add discretionary flags | 30 min | Significant savings |
| Convert poll to push | 2-4 hours | Largest impact |

## Symptom 5: Energy Spike During Specific Action

Noticeable battery drain or heat when performing particular operation.

### Diagnosis Decision Tree

```
Energy spike during specific action?
│
├─ Step 1: Record Power Profiler during action
│  └─ Note which subsystem spikes (CPU/GPU/Network/Display)
│
├─ CPU spike?
│  │
│  ├─ Is it parsing data?
│  │  ├─ Same data parsed repeatedly?
│  │  │  └─ Fix: Cache parsed results (lazy var)
│  │  └─ Large JSON/XML payload?
│  │     └─ Fix: Paginate, stream parse, or use binary format
│  │
│  ├─ Is it creating views?
│  │  ├─ Many views at once?
│  │  │  └─ Fix: Use LazyVStack/LazyHStack
│  │  └─ Complex view hierarchies?
│  │     └─ Fix: Simplify, use drawingGroup()
│  │
│  └─ Is it image processing?
│     ├─ On main thread?
│     │  └─ Fix: Move to background queue
│     └─ No caching?
│        └─ Fix: Cache processed images
│
├─ GPU spike?
│  │
│  ├─ Starting animation?
│  │  └─ Fix: Ensure frame rate appropriate
│  │
│  ├─ Showing blur effect?
│  │  └─ Fix: Use solid color or pre-rendered blur
│  │
│  └─ Complex render? (shadows, masks, many layers)
│     └─ Fix: Simplify, use shouldRasterize, cache
│
├─ Network spike?
│  │
│  ├─ Large download started?
│  │  └─ Fix: Use background URLSession, show progress
│  │
│  ├─ Many parallel requests?
│  │  └─ Fix: Limit concurrency, batch
│  │
│  └─ Retrying failed requests?
│     └─ Fix: Exponential backoff, waitsForConnectivity
│
└─ Display spike?
   └─ Unusual unless changing brightness programmatically
      └─ Fix: Don't modify brightness, let system control
```

### Time-Cost Analysis

| Approach | Time | Outcome |
|----------|------|---------|
| Power Profiler during action | 5-10 min | Identifies subsystem |
| Time Profiler for CPU details | 10-15 min | Identifies function |
| Code review without profiling | 1+ hours | May miss actual cause |

## Quick Diagnostic Checklist

Use this when you need fast answers:

### 30-Second Check

- [ ] Device plugged in? (Power metrics show 0)
- [ ] Debug build? (Less optimized than release)
- [ ] Low Power Mode on? (May affect measurements)

### 5-Minute Check (Power Profiler)

- [ ] Which subsystem is dominant? (CPU/GPU/Network/Display)
- [ ] Sustained or spiky?
- [ ] Foreground or background?

### 15-Minute Investigation

- [ ] If CPU: Run Time Profiler to identify function
- [ ] If Network: Check request frequency and size
- [ ] If GPU: Check animation frame rates
- [ ] If Background: Check Info.plist modes

### Common Quick Fixes

| Finding | Quick Fix | Time |
|---------|-----------|------|
| Timer without tolerance | Add `.tolerance = 0.1` | 1 min |
| VStack with large ForEach | Change to LazyVStack | 1 min |
| allowsExpensiveNetworkAccess = true | Set to false | 1 min |
| Missing stopUpdatingLocation | Add stop call | 2 min |
| No Dark Mode | Add asset variants | 30 min |
| Audio session always active | Add setActive(false) | 5 min |

## When to Escalate

### Use `energy` skill when

- Need full audit checklist
- Want comprehensive patterns with code
- Planning proactive optimization

### Use `energy-ref` skill when

- Need specific API details
- Want complete code examples
- Implementing from scratch

### Use `energy-auditor` agent when

- Want automated codebase scan
- Looking for anti-patterns at scale
- Pre-release energy audit

Run: `/axiom:audit energy`

---

## Version History

- **1.0.0**: Initial diagnostic skill covering 5 symptoms (Battery Settings, Device Hot, Background Drain, Cellular Drain, Action Spike) with decision trees, time-cost analysis, quick diagnostic checklist, and escalation guidance.

---

**Created** 2025-12-26
**Targets** iOS 26+
**Framework** Power Profiler, Instruments
