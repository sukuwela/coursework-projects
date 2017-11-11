# Shanaya Ukuwela 56649043


class steps:
    def steps(self, json_text):
        try:
            narrative_list = []
            for element in json_text['route']['legs']:
                for element2 in element['maneuvers']:
                    narrative_list.append(element2['narrative'])
            narrative_str = ''
            for narrative in narrative_list:
                narrative_str += narrative + '\n'
            print('\n'+'DIRECTIONS' + '\n' + narrative_str[:-1])
            print()

        except KeyError:
            print('\nNO ROUTE FOUND.')

class total_distance:
    def generate(self, json_text):
        
        try:
            total_distance = json_text['route']['distance']
            print("\nTOTAL DISTANCE: {} miles".format(round(total_distance)))
        except KeyError:
            print('\nNO ROUTE FOUND.')
            
class total_time:
    def generate(self, json_text):
    
        try:
            total_time = json_text['route']['time']
            print("\nTOTAL TIME: {} minutes".format(round(total_time/60)))
            print()
        except KeyError:
            print('\nNO ROUTE FOUND.')

class latLng:
    def order(self, latLng_str):
        try:
            latLng_list = latLng_str[:-1].split(',')
            output_str = ''
            for element in latLng_list:
                if latLng_list.index(element)%2 == 0:
                    if float(element) > 0:
                        output_str += "{:.2f}N ".format(float(element))
                    else:
                        output_str += "{:.2f}S ".format(float(element[1:]))
                elif latLng_list.index(element)%2 != 0:
                    if float(element) > 0:
                        output_str += "{:.2f}E\n".format(float(element))
                    else:
                       output_str += "{:.2f}W\n".format(float(element[1:]))
            print('\nLATLONGS' + '\n' + output_str[:-1])
        except KeyError:
            print("\nNO ROUTE FOUND.")

class elevation:
    def generate(self, json_text):
        try:
            elevation_str = ''
            for element in json_text['elevationProfile']:
                elevation_str += str(round((element['height'])*3.2808)) + '\n'
            print('\nELEVATIONS' + '\n' + elevation_str)
        except KeyError:
            print("\nNO ROUTE FOUND.")

