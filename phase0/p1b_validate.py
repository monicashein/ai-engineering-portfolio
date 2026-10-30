"""P1b lab: booleans, None, control flow and truthiness on synthetic meter readings."""

readings = [120.5, 0, None, -3.2, 950.0, 85.25, None, 0.0]
high_threshold = 500

missing = zero = invalid = high = normal = 0   # counters

for i, r in enumerate(readings, start=1):
    # TODO 1: classify r using if / elif / else, in this exact priority:
    if r is None:
        status = "MISSING"
        missing += 1
    elif r < 0:
        status = "INVALID"
        invalid += 1
    elif not r:  # handles both 0 and 0.0
        status = "ZERO"
        zero += 1
    elif r > high_threshold:
        status = "HIGH"
        high += 1
    else:
        status = "NORMAL"
        normal += 1

    # TODO 2: print one line per reading, e.g.  "#1  120.5  NORMAL"
    #         show "-" instead of the value when r is None (use a conditional expression)
    val_display = "-" if r is None else r
    print(f"#{i:<2} {val_display:<7} {status}")

# TODO 3: print the summary line:
print(f"MISSING={missing} INVALID={invalid} ZERO={zero} HIGH={high} NORMAL={normal}")

# TODO 4: print "ALERT: data quality check failed" if there is any MISSING or INVALID reading,
#         otherwise "Data quality OK"
if missing > 0 or invalid > 0:
    print("ALERT: data quality check failed")
else:
    print("Data quality OK")
