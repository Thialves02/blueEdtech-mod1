mes = {'1':"janeiro",'2':"fevereiro",'3':"março",'4':'abril','5':'maio','6':'junho','7':'julho','8':'agosto','9':'setembro','10':'outubro','11':'novembro','12':'dezembro'}
l = {}

data = input("Digite a data = ")

def data1(data): 
    l['data'] = data
    if l['data'][3:5] == '01':
        return f'A data extensa é {l["data"][:2]} de {mes["1"]} de {l["data"][6:]}'
    if l['data'][3:5] == '02':
        return f'A data extensa é {l["data"][:2]} de {mes["2"]} de {l["data"][6:]}'
    if l['data'][3:5] == '03':
        return f'A data extensa é {l["data"][:2]} de {mes["3"]} de {l["data"][6:]}'
    if l['data'][3:5] == '04':
        return f'A data extensa é {l["data"][:2]} de {mes["4"]} de {l["data"][6:]}'
    if l['data'][3:5] == '05':
        return f'A data extensa é {l["data"][:2]} de {mes["5"]} de {l["data"][6:]}'
    if l['data'][3:5] == '06':
        return f'A data extensa é {l["data"][:2]} de {mes["6"]} de {l["data"][6:]}'
    if l['data'][3:5] == '07':
        return f'A data extensa é {l["data"][:2]} de {mes["7"]} de {l["data"][6:]}'
    if l['data'][3:5] == '08':
        return f'A data extensa é {l["data"][:2]} de {mes["8"]} de {l["data"][6:]}'
    if l['data'][3:5] == '09':
        return f'A data extensa é {l["data"][:2]} de {mes["9"]} de {l["data"][6:]}'
    if l['data'][3:5] == '10':
        return f'A data extensa é {l["data"][:2]} de {mes["10"]} de {l["data"][6:]}'
    if l['data'][3:5] == '11':
        return f'A data extensa é {l["data"][:2]} de {mes["11"]} de {l["data"][6:]}'
    if l['data'][3:5] == '12':
        return f'A data extensa é {l["data"][:2]} de {mes["12"]} de {l["data"][6:]}'
    
 
print(data1(data))


