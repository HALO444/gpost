import os
import requests
import concurrent.futures

def user():
    print("* To get help gpost --help")
    print("Example : gpost https://example.com/ '/home/gpost/Downloads/w_list.txt'")
    print()
    user_input = input("  >>> ")
    user_input = user_input.strip().split()
    
    if user_input == []:
        end()
    elif user_input[0].lower() != "gpost":
        print(f'Error: "gpost" Not {user_input[0]}')
        end()  
    elif user_input[1] == "--help" or user_input[1] == "-h":
        help()
    else:
        run(user_input)

def run(user_input):
    os_cm = f"cp {user_input[2]} list.txt"
    os.system(os_cm)
    with open("list.txt", 'r') as w_list:
        word_list = [line.strip() for line in w_list]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_url, user_input[1], word) for word in word_list]
        for future in concurrent.futures.as_completed(futures):
            url, status_code = future.result()
            if status_code != 404:
               if  status_code != 500 : 
                  print(f'{url}: [{status_code}]')
               else:
                   print(f'[{status_code}]')   
            #else:
                
               #print(f'[{status_code}]')
def fetch_url(base_url, word):
    url = base_url + word
    response = requests.get(url)
    return url, response.status_code

def help():
    art = '''                                   
    mmm  mmmmm                  m   
 m"   " #   "#  mmm    mmm   mm#mm 
 #   mm #mmm#" #" "#  #   "    #   
 #    # #      #   #   """m    #   
  "mmm" #      "#m#"  "mmm"    "mm 
                                   
     by HALO44O
     github :  https://github.com/HALO444                             
                                                                                
'''
    print(art)
    print()

    help_l = '''
      gpost [url] ['path/to/list.txt']
       
''' 
    print(help_l)

def end():
    print()

user()
