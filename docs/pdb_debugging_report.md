# PDB Debugging Report

## Program investigated

`gps-plotter.py` from the supplied `MMA3001-Buggy-Code` repository.

## Repository version

- Commit: `9294a6c54b695807585fb26b0cea725d6d04b26a`
- Debugging mode: `current-coordinate-validation`

## Initial behaviour

The GPS data file contains invalid geographic coordinates. The current version of the program detects these records and prevents them from being plotted.

## Debugging method

The program was started using:

```text
python -m pdb gps-plotter.py
```

The conditional breakpoint was:

```text
b 21, math.isnan(lat) or abs(lat) > 90 or abs(lon) > 180
```

Execution was continued using `c`. The commands `l`, `p lat`, `p lon`, `pp locals()`, and `n` were used to inspect the program.

The complete debugger output is stored in:

```text
reports/pdb_session.txt
```

## Debugger findings

- Relevant variable: `lat`
- Incorrect value: 95.9871116971152 at GPS data line 412, with longitude 10.303389172138218
- Expected value or range: Latitude must remain between -90 and 90 degrees. Longitude must remain between -180 and 180 degrees.

The GPS-data scan also found:

- Line 412: latitude `95.9871116971152`
- Line 480: latitude `NaN`

## Cause of the issue

The input file contains an invalid latitude greater than 90 degrees. It also contains a later record whose latitude is NaN.

## Required correction

Validate every parsed coordinate before appending it to the plotting list. Skip NaN values, latitude outside ±90 degrees, and longitude outside ±180 degrees.

## Relevant source-code context

```python
  13:         list[tuple[float, float]]: A list of (latitude, longitude) tuples for valid GPS points.
  14:             Invalid points (NaN latitude, latitude > 90, or longitude > 180) are skipped.
  15:     """
  16:     coords = []
  17:     with open(filename) as f:
  18:         for line in f:
  19:             lat, lon = line.strip().split(',')
  20:             lat, lon = float(lat), float(lon)
  21:             if math.isnan(lat) or abs(lat) > 90 or abs(lon) > 180:
  22:                 continue
  23:             coords.append((lat, lon))
  24:     return coords
  25: 
  26: # --- Step 2: Plot on world map ---
  27: def plot_gps_points(coords, map_image="Plate-Carree-Projection.png"):
  28:     """Plots a list of GPS coordinates on a world map image.
  29: 
```

## Conclusion

The conditional breakpoint stopped execution when the invalid coordinate was being processed. This exposed the incorrect latitude without requiring manual stepping through every earlier record. The current source includes validation that skips the invalid data before plotting.
