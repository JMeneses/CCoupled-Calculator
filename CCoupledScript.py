import math, cmath, numpy

# Resistance Calculation
def calculate_resistance_ohms(resistivity, height, area):
    R = (resistivity*height)/area
    return R

# Capacitance Calculation
def calculate_capacitance_farads(relative_permitivity, height, area):
    e0 = 8.8542*1e-12
    C = (e0*relative_permitivity*area)/height
    return C

# Impedance Calculation
def calculate_reactance_capacitor(C, frequency_Hz):
    Xc = -1/(2*math.pi*frequency_Hz*C)
    return Xc

# RC Impedance Calculation
def calculate_combined_impedance_parallel_rc(Rr, Xc):
    Zr = complex(Rr,0)
    Zc = complex(0,Xc) 
    Zrc = (Zr*Zc)/(Zr+Zc)
    return Zrc

# Global Method
def calculate_electric_field(radius,i1_c,i1_e,i1_h,cm_c,cm_e,cm_h,i2_c,i2_e,i2_h,freq,ampl,isPulse,rise_t):
    result_ef_string = ""
    result_string = ""
    radius = radius/1000
    i1_h = i1_h/1000
    cm_h = cm_h/1000
    i2_h = i2_h/1000
    # 1st Layer
    R_i1 = calculate_resistance_ohms(1/i1_c, i1_h, math.pi*pow(radius,2))
    C_i1 = calculate_capacitance_farads(i1_e, i1_h, math.pi*pow(radius,2))
    # 2nd Layer
    R_cm = calculate_resistance_ohms(1/cm_c, cm_h, math.pi*pow(radius,2))
    C_cm = calculate_capacitance_farads(cm_e, cm_h, math.pi*pow(radius,2))
    # 3rd Layer
    R_i2 = calculate_resistance_ohms(1/i2_c, i2_h, math.pi*pow(radius,2))
    C_i2 = calculate_capacitance_farads(i2_e, i2_h, math.pi*pow(radius,2))
    # Impedance of Individual Layers
    if (isPulse):
        freq = 1/(2*math.pi*rise_t) 
    Xc_i1 = calculate_reactance_capacitor(C_i1,freq)
    Xc_cm = calculate_reactance_capacitor(C_cm,freq)
    Xc_i2 = calculate_reactance_capacitor(C_i2,freq)
    Zrc_i1 = calculate_combined_impedance_parallel_rc(R_i1,Xc_i1)
    Zrc_cm = calculate_combined_impedance_parallel_rc(R_cm,Xc_cm)
    Zrc_i2 = calculate_combined_impedance_parallel_rc(R_i2,Xc_i2)
    result_string += "1st Layer - Electric Insulator \n"
    result_string += "  R = "+str('{:.3e}'.format(R_i1))+" Ohms \n"
    result_string += "  C = "+str('{:.3e}'.format(C_i1))+" Farads \n"
    result_string += "  Xc = "+str('{:.3e}'.format(Xc_i1))+" Ohms \n"
    result_string += "\n2nd Layer - Culture Medium \n"
    result_string += "  R = "+str('{:.3e}'.format(R_cm))+" Ohms \n"
    result_string += "  C = "+str('{:.3e}'.format(C_cm))+" Farads \n"
    result_string += "  Xc = "+str('{:.3e}'.format(Xc_cm))+" Ohms \n"
    result_string += "\n3rd Layer - Electric Insulator \n"
    result_string += "  R = "+str('{:.3e}'.format(R_i2))+" Ohms \n"
    result_string += "  C = "+str('{:.3e}'.format(C_i2))+" Farads \n"
    result_string += "  Xc = "+str('{:.3e}'.format(Xc_i2))+" Ohms \n"
    # Total Impedance of the Layers in Series
    Zrc_series = Zrc_i1+Zrc_cm+Zrc_i2
    result_string += "\nAll Layers in Series \n"
    result_string += "  Zrc_series: "+str('{:.3e}'.format(Zrc_series))+"\n"
    result_string += "  Zrc_series Magnitude: "+str('{:.3e}'.format(abs(Zrc_series)))+"\n"
    result_string += "  Zrc_series Phase: "+str('{:.3e}'.format(numpy.degrees(cmath.phase(Zrc_series))))+"\n"
    I = ampl/abs(Zrc_series)
    Em = (I*abs(Zrc_cm))/cm_h
    result_string += "\nElectric Current in the CCoupled System \n"
    result_string += "  I: "+str('{:.3e}'.format(I))+" A"
    result_string += "\nElectric Field in Culture Medium \n"
    result_string += "  Em: "+str('{:.3e}'.format(Em))+" V/m"
    result_ef_string += "Em: "+str('{:.2e}'.format(Em))+" V/m"
    return result_ef_string, result_string
