import sys
import bouncing_dvd_logo as blogo

try:
    blogo.main()

except KeyboardInterrupt:
    print()
    print("Bouncing DVD logo")
    sys.exit()
