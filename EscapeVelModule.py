def EscapeVel(planet_mass, planet_radius):

    #This is a module to compute escape velocities for planets

    # Here is the relevant equation: V_esc = sqrt( 2 * G * M / r)

    #Start by defining Newton's Gravitational Constant

    grav_const = 6.672 * (10. ** -11.)

    # Now to do the actual calculation

    escape_vel = ((2. * grav_const * planet_mass) / planet_radius) ** 0.5

    return escape_vel
