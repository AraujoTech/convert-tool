import pyinputplus as pyip
import os

database_url = os.environ.get('DATABASE_URL', 'sqlite:///')

def convert_to_cpu(type='mili',value=0):
    
    if type == 'mili':
        return value/1000
    elif type == 'nano':
        return value/1000000000

def convert_from_cpu_to_mili(value):
    return value*1000

def convert_from_cpu_to_nano(value):
    return value*1000000000

def convert_from_mili_to_nano(value):
    cpu = convert_to_cpu('mili', value)
    nano = convert_from_cpu_to_nano(cpu)
    return nano

def convert_from_nano_to_mili(value):
    cpu = convert_to_cpu('nano', value)
    mili = convert_from_cpu_to_mili(cpu)
    return mili
def convert_cpu():
    convert_type=pyip.inputMenu(['from mili to cpu', 'from mili to nano','from nano to cpu', 'from nano to mili', 'from cpu to mili', 'from cpu to nano'],numbered=True)
    value=pyip.inputNum(prompt='Put the value to convert: ', greaterThan=0)
    if convert_type == 'from mili to cpu':
        result=convert_to_cpu('mili',value)
        print(f"Result:\t{result:,}")
        return result
    if convert_type == 'from mili to nano':
        result=convert_from_mili_to_nano(value)
        print(f"Result:\t{result:,}n")
        return result
    if convert_type == 'from nano to cpu':
        result=convert_to_cpu('nano',value)
        print(f"Result:\t{result:,}")
        return result
    if convert_type == 'from nano to mili':
        result=convert_from_nano_to_mili(value)
        print(f"Result:\t{result:,}m")
        return result
    if convert_type == 'from cpu to mili':
        result=convert_from_cpu_to_mili(value)
        print(f"Result:\t{result:,}m")
        return result
    if convert_type == 'from cpu to nano':
        result=convert_from_cpu_to_nano(value)
        print(f"Result:\t{result:,}n")
        return result
    
def convert_gb_to_b(value):
    return value * 1073741824
def convert_mb_to_gb(value):
    return value/1024

def convert_memory():
    convert_type=pyip.inputMenu(['from gb to byte','from mb to byte'],numbered=True)
    value=pyip.inputNum(prompt='Put the value to convert: ', greaterThan=0)
    
    if convert_type == 'from gb to byte':
        result=convert_gb_to_b(value)
        print(f"Result:\t{result:,}b")
        return result
    
    if convert_type == 'from mb to byte':
        result=convert_mb_to_gb(value)
        result=convert_gb_to_b(result)        
        print(f"Result:\t{result:,}b")
        return result
    

def main():
    initial_menu = pyip.inputMenu(['get CPU recommendations','get Memory recommendations', 'get all recommendations'],numbered=True)
    
    if initial_menu == 'get CPU recommendations':
        cpu=convert_cpu()
        recommendation_data={
        "CPU":{"critical":{"alert":cpu*0.9,"recovery": cpu*0.8},"warn":{"alert":cpu*0.8,"recovery": cpu*0.75}}
        }
        recommendation=f"\n========== Recommended CPU Alerts\n\n Critical:\n Alert: {recommendation_data ['CPU']['critical']['alert']} \n Recovery: {recommendation_data ['CPU']['critical']['recovery']} \n\n Warn:\n Alert: {recommendation_data ['CPU']['warn']['alert']} \n Recovery: {recommendation_data ['CPU']['warn']['recovery']} \n\n"
        print (recommendation)
        return recommendation_data
    if initial_menu == 'get Memory recommendations':
        memory=convert_memory()
        recommendation_data={
           "Memory":{"critical":{"alert":memory*0.9,"recovery": memory*0.8},"warn":{"alert":memory*0.8,"recovery": memory*0.75}}
        }
        recommendation=f"\n========== Recommended Memory Alerts\n\n Critical:\n Alert: {recommendation_data ['Memory']['critical']['alert']} \n Recovery: {recommendation_data ['Memory']['critical']['recovery']} \n\n Warn:\n Alert: {recommendation_data ['Memory']['warn']['alert']} \n Recovery: {recommendation_data ['Memory']['warn']['recovery']} \n\n"
        print (recommendation)
        return recommendation_data
    
    if initial_menu == 'get all recommendations':
        cpu=convert_cpu()
        memory=convert_memory()
        recommendation_data={
            "CPU":{"critical":{"alert":cpu*0.9,"recovery": cpu*0.8},"warn":{"alert":cpu*0.8,"recovery": cpu*0.75}},
            "Memory":{"critical":{"alert":memory*0.9,"recovery": memory*0.8},"warn":{"alert":memory*0.8,"recovery": memory*0.75}}
        }
        recommendation=f"\n========== Recommended CPU Alerts\n\n Critical:\n Alert: {recommendation_data ['CPU']['critical']['alert']} \n Recovery: {recommendation_data ['CPU']['critical']['recovery']} \n\n Warn:\n Alert: {recommendation_data ['CPU']['warn']['alert']} \n Recovery: {recommendation_data ['CPU']['warn']['recovery']} \n\n========== Recommended Memory Alerts\n\n Critical:\n Alert: {recommendation_data ['Memory']['critical']['alert']} \n Recovery: {recommendation_data ['Memory']['critical']['recovery']} \n\n Warn:\n Alert: {recommendation_data ['Memory']['warn']['alert']} \n Recovery: {recommendation_data ['Memory']['warn']['recovery']} \n\n"
        print (recommendation)
        return recommendation_data
    
    
     
if __name__ == '__main__':
    main()