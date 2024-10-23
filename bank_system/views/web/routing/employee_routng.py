from models.client import Individual, Account, Client
from views.web.utils.color_utils import decode_colors

def employee_root(root_path: str, query_params: dict[str, list[str]] = {} ) -> tuple[str, str, str, str, str, str, str]:
    main_title: str ="Employee title"
    main_content: str ="Employee content"
    page_title: str ="Pagina de funcionários:"
    script_js: str = ""
    
    return (
        page_title,
        main_title, 
        main_content, 
        script_js,
        f"{root_path}/header.html",
        f"{root_path}/employee/nav.html", 
        f"{root_path}/generic_main.html"
    )
    
   
 
def employee_new_client(root_path: str, query_params: dict[str, list[str]] = {}) -> tuple[str, str, str, str, str, str, str]:
    print(query_params)
    main_title: str ="Cadastre um novo cliente aqui:"
    main_content: str =""
    page_title: str ="Pagina de funcionários:"
    script_js: str = ""
    
    new_cpf = query_params.get('new_cpf', [""])[0]
    name = query_params.get('name', [""])[0].strip('"')
    date_of_birth = query_params.get('date_of_birth', [""])[0].strip('"')
    address = query_params.get('address', [""])[0].strip('"')
    create_new_account = bool(query_params.get('create_new_account', ["True"])[0])
    
    
    client, msg = Individual.create_new_client(new_cpf, name, date_of_birth, address, create_new_account)
    if client:
        client_json = client.to_json()
    else:
        client_json = "{}"
    
    msg = decode_colors(msg)
    main_content = f"""
        
        <div class="yellow" style="font-size: 25px">
        {msg}
        <br />
        <div>
        <br />
            <div class="yellow" style="font-size: 25px; color: blue;">
                Dados recebidos pelo servidor:
            </div>

            <br>
            <span class="yellow">CPF:</span> <span class="green">{new_cpf}</span>
            <br>
            <span class="yellow">Nome: </span> <span class="green">{name}</span>
            <br>
            <span class="yellow">Data de Nascimento: </span> <span class="green">{date_of_birth}</span>
            <br>
            <span class="yellow">Endereço: </span> <span class="green">{address}</span>
            <br>
            <span class="yellow">Conta Nova: </span> <span class="green">{create_new_account}</span>
        </div>
        
        <script>
          
          
          

        </script>
    """
    
    script_js = f"""
<script>

  const client_json = { client_json }
  console.log(client_json)

  try {{
 
    if (client_json._id !== '?' && client_json._id !== undefined) {{
      // Check if data exists
      console.log("Client JSON:", client_json) // Log the entire object for inspection
      localStorage.setItem("cliente", JSON.stringify(client_json))
    }}
    storedClient = JSON.parse(localStorage.getItem("cliente")) // Parse first!

    if (storedClient) {{
      // Check if data exists
      console.log("Stored Client:", storedClient) // Log the entire object for inspection

      // Now access properties safely
      console.log("ID:", storedClient._id)
      console.log("Date of Birth:", storedClient._date_of_birth)

    }} else {{
      console.error("No client data found in local storage.")
    }}
  }} catch (error) {{
    console.error("Error storing or retrieving client data:", error)
  }}


    document.addEventListener("DOMContentLoaded", function() {{
        const form = document.getElementById("fm_new_client");
          if (form) {{ 
            form.addEventListener("submit", function(event) {{
                event.preventDefault();
                
                
      
        storedClient = JSON.parse(localStorage.getItem("cliente"))
        if (storedClient) {{
            document.getElementById("user_selected").innerHTML = `
            Usuário: ${{storedClient._name}}
            <br />
            CPF: ${{storedClient._id}}
        `
        }} else {{
            document.getElementById("user_selected").innerHTML = ""
        }}
                
                
            }});
          }} else {{
            console.error("Form 'fm_new_client' element not found!"); // Helpful debugging message
          }}
          
          const button = document.getElementById("bt_save");
          if (button) {{ // Check if the button exists
            button.addEventListener("click", function () {{
              form.submit();
              
              
        
        
              
              
            }});
          }} else {{
            console.error("Button element not found!"); // Helpful debugging message
          }}
    }})
    

 
</script>
"""
    
    return (
        page_title,
        main_title, 
        main_content, 
        script_js,
        f"{root_path}/header.html",
        f"{root_path}/employee/nav.html", 
        f"{root_path}/employee/form_new_client.html",
    )
    
def employee_new_account(root_path: str, query_params: dict[str, list[str]] = {}) -> tuple[str, str, str, str, str, str, str]:
    main_title: str ="Nova conta:"
    main_content: str ="Employee content"
    page_title: str ="Pagina de criada de novas contas"
    script_js: str = ""
    
    cpf = query_params.get("cpf", [""])[0]
    client: Individual = Individual.get_client(cpf)
    
    if(client):
        client.create_account()
        main_content = client.get_str_client()
        main_content = decode_colors(main_content)
    elif(cpf != ""):
        main_content = f"<span class='red'>Cliente de CPF <span class='yellow'>{cpf}</span> não encontrado! Faça seu cadastro.</span>"
    else:
        main_content = "<span class='red'>Nenhum cliente selecionado, preencha o campo CPF e refaça a busca!</span>"
   
    
    
    return (
        page_title,
        main_title, 
        main_content, 
        script_js,
        f"{root_path}/header.html",
        f"{root_path}/employee/nav.html", 
        f"{root_path}/generic_main.html"
    )
    
    
def employee_client_select(root_path: str, query_params: dict[str, list[str]] = {}) -> tuple[str, str, str, str, str, str, str]:
    main_title: str ="Cliente:"
    main_content: str ="cliente"
    page_title: str ="Pagina de ciente selecionado"
    script_js: str = ""
    
    cpf = query_params.get("cpf", [""])[0]
    client: Individual = Individual.get_client(cpf)
    
    client_json = {}
    if(client):
        client_json = client.to_json()
    
    if client:
        script_js = client.to_json()
        script_js =  f"""<script>
        
  const client_json = { client_json }
  console.log(client_json)

  try {{
 
    if (client_json._id !== '?' && client_json._id !== undefined) {{
      // Check if data exists
      console.log("Client JSON:", client_json) // Log the entire object for inspection
      localStorage.setItem("cliente", JSON.stringify(client_json))
    }}
    storedClient = JSON.parse(localStorage.getItem("cliente")) // Parse first!

    if (storedClient) {{
      // Check if data exists
      console.log("Stored Client:", storedClient) // Log the entire object for inspection

      // Now access properties safely
      console.log("ID:", storedClient._id)
      console.log("Date of Birth:", storedClient._date_of_birth)

    }} else {{
      console.error("No client data found in local storage.")
    }}
  }} catch (error) {{
    console.error("Error storing or retrieving client data:", error)
  }}
        
        </script>"""
    
    if(client):
        main_content = client.get_str_client()
        main_content = decode_colors(main_content)
    elif(cpf != ""):
        main_content = f"<span class='red'>Cliente de CPF <span class='yellow'>{cpf}</span> não encontrado! Faça seu cadastro.</span>"
    else:
        main_content = "<span class='red'>Nenhum cliente selecionado, preencha o campo CPF e refaça a busca!</span>"
    return (
        page_title,
        main_title, 
        main_content, 
        script_js,
        f"{root_path}/header.html",
        f"{root_path}/employee/nav.html", 
        f"{root_path}/generic_main.html"
    )
    

def employee_clients_list(root_path: str, query_params: dict[str, list[str]] = {}) -> tuple[str, str, str, str, str, str, str]:
    main_title: str ="Lista de clientes:"
    main_content: str ="cliente"
    page_title: str ="Pagina de cientes"
    script_js: str = ""
    
    main_content = Client.get_str_clients()
    main_content = decode_colors(main_content)
    
    return (
        page_title,
        main_title, 
        main_content, 
        script_js,
        f"{root_path}/header.html",
        f"{root_path}/employee/nav.html", 
        f"{root_path}/generic_main.html"
    )
    
    
def employee_account_list(root_path: str, query_params: dict[str, list[str]] = {}) -> tuple[str, str, str, str, str, str, str]:
    main_title: str ="Lista de contas:"
    main_content: str ="contas"
    page_title: str ="Pagina de contas"
    script_js: str = ""
    
    main_content = Account.get_str_accounts()
    main_content = decode_colors(main_content)
    
    return (
        page_title,
        main_title, 
        main_content, 
        script_js ,
        f"{root_path}/header.html",
        f"{root_path}/employee/nav.html", 
        f"{root_path}/generic_main.html"
    )