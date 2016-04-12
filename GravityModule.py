def SurfaceGravity(planet_mass, planet_radius):

    #This is HypoPlanet in module form

    #Define Newton's gravitational constant

    grav_constant = 6.672 * (10. ** -11.)

    # a_g = G*M / r^2

    surface_grav = planet_mass * grav_constant / (planet_radius**2.)

    return surface_grav
