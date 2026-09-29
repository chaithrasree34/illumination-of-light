# illumination-of-light
# Python program to calculate illumination of light

I = float(input("Enter luminous intensity (in candela): "))
d = float(input("Enter distance from light source (in meters): "))

# Calculate illumination
E = I / (d ** 2)

print("Illumination of light =", E, "lux")

Example

Input:

Enter luminous intensity (in candela): 100
Enter distance from light source (in meters): 5


Output:

Illumination of light = 4.0 lux
