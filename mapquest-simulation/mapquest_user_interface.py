# Shanaya Ukuwela. ID: 56649043

import mapquest_output as output
import api_interaction as api

location_list = []
generator_list = []

def location_input():

    try:
        num_loc = int(input())
        if num_loc < 2:
            print("You must specify two locations to run this experiment")
        elif num_loc >= 2:
            for num in range(num_loc):
                location_list.append(input())
            return location_list
    except ValueError:
        print("The first line must specify a positive integer number of locations.")

def generator_input():

    try:
        gen_num = int(input())
        if gen_num == 0 or gen_num > 5:
            print("There must be a positive integer number of generators "+\
                  "less than or equal to 5.")
        elif gen_num <= 5:
            for gen_num in range(gen_num):
                generator_list.append(input())
    except ValueError:
        print("There must be a positive integer number of generators "+\
                  "less than or equal to 5.")
    
    return generator_list

            
def user_interface():
    try:
        loc_list = location_input()
        gen_list = generator_input()
        json_text = api.get_json(api.directions_url(loc_list))
        for gen in gen_list:
            if gen == "STEPS":
                directions = output.steps()
                directions.steps(json_text)
            elif gen == "TOTALDISTANCE":
                total_distance = output.total_distance()
                total_distance.generate(json_text)
            elif gen == "TOTALTIME":
                total_time = output.total_time()
                total_time.generate(json_text)
            elif gen == "LATLONG":
                latLng_str = api.get_latLngs(json_text)
                latLng_output = output.latLng()
                latLng_output.order(latLng_str)
            elif gen == "ELEVATION":
                latLng_str = api.get_latLngs(json_text)
                json_elev_text = api.get_json(api.elevations_url(latLng_str))
                elevation_output = output.elevation()
                elevation_output.generate(json_elev_text)
            else:
                print("Invalid input.")
                break
    except KeyError:
         return
    except:
        print('\nMAPQUEST ERROR.')
            
    else:
        print("\nDirections Courtesy of MapQuest; Map" +\
              "Data Copyright OpenStreetMap Contributors")

if __name__ == '__main__':
    user_interface()
        
