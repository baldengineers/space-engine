#SCALE:
#1 light year = 63241.1 AU  - 948616500 GL units
#1 AU = 150,000,000 km      - 15000 GL units
#1km = 0.0001 units in GL
#1m = 0.000001 GL units

#UNIT LIST:
# 'km'= kilometer
# 'm' = meter
# 'au'= astronomical unit
# 'ly'= lightyear

def convert(input_value,units_in='',units_out=''):
    glu_dict = {'km':0.0001,
                'm':0.000001,
                'au':15000,
                'ly':948616500}
    o = glu_dict[units_in]/glu_dict[units_out]

    return o, str(o,units_out)

def compare():
    pass
    
