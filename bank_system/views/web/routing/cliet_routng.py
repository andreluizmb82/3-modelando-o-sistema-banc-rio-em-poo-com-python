from models.account import Account
from views.web.utils.color_utils import decode_colors

def client(root_path: str, query_params: dict[str, list[str]] = {} ) -> tuple[str, str, str, str, str, str, str]:
     main_title: str =""
     main_content: str =""
     page_title: str =""
     script_js: str = ""

     return (
          page_title,
          main_title, 
          main_content, 
          script_js,
          f"{root_path}/header.html",
          f"{root_path}/client/nav.html", 
          f"{root_path}/generic_main.html"
     )
    
def client_select_account(root_path: str, query_params: dict[str, list[str]] = {} ) -> tuple[str, str, str, str, str, str, str]:
     main_title: str ="Selecione uma conta:"
     main_content: str =""
     page_title: str ="Pagina de contas:"
     script_js: str = "" #"<script>const account_json = {}</script>"


     account_number = int(query_params.get("account_number", [0])[0])
     account = None
     try:
          account = Account.get_account(account_number)
          account_json = f"const account_json = {{cpf: '{account.cpf_client}', account_number: '{account.account_number}', bank_branch: '{account.bank_branch}', balance: '{account.balance}'}}"
          script_js = f"<script>{account_json}</script>"
     except ValueError as exp:
          main_content = decode_colors(str(exp))
     return (
          page_title,
          main_title, 
          main_content, 
          script_js,
          f"{root_path}/header.html",
          f"{root_path}/client/nav.html", 
          f"{root_path}/generic_main.html"
     )
    
def client_deposit(root_path: str, query_params: dict[str, list[str]] = {} ) -> tuple[str, str, str, str, str, str, str]:
     main_title: str =""
     main_content: str =""
     page_title: str ="Pagina de depósitos:"
     script_js: str = ""

     account_number = int(query_params.get("account_number", [0])[0])
     value = int(query_params.get("deposit_value", [0])[0])
     
     try:
          account: Account = Account.get_account(account_number)
          main_content = decode_colors(account.deposit(value))
          
          account_json = f"const account_json = {{cpf: '{account.cpf_client}', account_number: '{account.account_number}', bank_branch: '{account.bank_branch}', balance: '{account.balance}'}}"
          script_js = f"<script>{account_json}</script>"
     except ValueError as exp:
          main_content = decode_colors(str(exp))
    
          
     return (
          page_title,
          main_title, 
          main_content, 
          script_js,
          f"{root_path}/header.html",
          f"{root_path}/client/nav.html", 
          f"{root_path}/generic_main.html"
    )
    
def client_withdraw(root_path: str, query_params: dict[str, list[str]] = {} ) -> tuple[str, str, str, str, str, str, str]:
     main_title: str =""
     main_content: str =""
     page_title: str ="Pagina de saques:"
     script_js: str = ""
    
     account_number = int(query_params.get("account_number", [0])[0])
     value = int(query_params.get("withdraw_value", [0])[0])
     
     try:
          account: Account = Account.get_account(account_number)
          main_content = decode_colors(account.withdraw(value))
          
          account_json = f"const account_json = {{cpf: '{account.cpf_client}', account_number: '{account.account_number}', bank_branch: '{account.bank_branch}', balance: '{account.balance}'}}"
          script_js = f"<script>{account_json}</script>"
     except ValueError as exp:
          main_content = decode_colors(str(exp))
    
    
     return (
          page_title,
          main_title, 
          main_content, 
          script_js,
          f"{root_path}/header.html",
          f"{root_path}/client/nav.html", 
          f"{root_path}/generic_main.html"
    )
    
def client_statement(root_path: str, query_params: dict[str, list[str]] = {} ) -> tuple[str, str, str, str, str, str, str]:
     main_title: str ="Visualize seu extrato:"
     main_content: str =""
     page_title: str ="Pagina de extratos."
     script_js: str = ""
     
     account_number = int(query_params.get("account_number", [0])[0])
     print(account_number)
     try:
          account: Account = Account.get_account(account_number)
          main_content = decode_colors(account.get_statement())
     except ValueError as exp:
          main_content = decode_colors(str(exp))
          
    
     return (
          page_title,
          main_title, 
          main_content, 
          script_js,
          f"{root_path}/header.html",
          f"{root_path}/client/nav.html", 
          f"{root_path}/generic_main.html"
     )