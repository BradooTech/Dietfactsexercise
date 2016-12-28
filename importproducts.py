import xmlrpclib 
import csv



server = 'http://localhost:8069'
database = 'NewModuleDB'
user = 'admin'
pwd = 'admin'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(server))

print common.version()

uid = common.authenticate(database, user, pwd, {})

print uid

OdooApi = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(server))

product_count = OdooApi.execute_kw(database, uid, pwd,
                                   'res.users.meal',
                                   'search_read',
                                    [[['totalcalories','>',3000],['totalitems','<',4]]],
                                    {'fields':['name','meal_date','totalcalories','totalitems']})

print product_count

filename = 'importation.csv'
reader = csv.reader(open(filename,'rb'))

for row in reader:
    
    print row
    
    product_exists = OdooApi.execute_kw(database, uid, pwd,'product.template','search',[[['name','=',row[0]]]],)
    
    if product_exists:
        print product_exists       
        print "Product found!"
        
    else:
        print "Adicionando produto"
        OdooApi.execute_kw(database, uid, pwd,
                          'product.template',
                           'create',
                           [{'name':row[0],'calories':row[1],'servingsize':row[2],'categ_id':3}])
    
       
'''
product_count2 = OdooApi.execute_kw(database, uid, pwd,
                                   'product.template',
                                   'search_read',
                                    [[['categ_id','=',3]]],
                                    {'fields':['name','meal_date','totalcalories','totalitems']})



for prod in product_count2:
    if prod['name'] == 'ONUburger':
        print "Produto encontrado, ID = " ,prod['id'], "\nAlteracoes sendo realizadas..."

        OdooApi.execute_kw(database, uid, pwd,
                           'product.template','write',
                           [[prod['id']],{'calories':15000} ])
    else:
        print "Produto nao esta no ID " , prod['id']


for prod in product_count2:
    print "Procurando ",prod, " ..."
    
escolha = raw_input('qual produto quer deletar?\n')

print escolha
for prod in product_count2:
    if prod['name'] == escolha:
        print "Produto encontrado, ID = " ,prod['id']
        print "Produto sendo deletado"
        OdooApi.execute_kw(database, uid, pwd,
                           'product.template','unlink',
                           [[prod['id']]])
    else:
        print "Produto nao esta no ID " , prod['id']
'''


reports_ids = OdooApi.execute_kw(database, uid, pwd, 'product.template', 'search',[[['categ_id','=',3]]])
report = xmlrpclib.ServerProxy('{}/xmlrpc/2/report'.format(server))
result = report.render_report(database, uid, pwd, 'product.nutrition', reports_ids)
report_data = result['result'].decode('base64')

arquivo = open('relatorio.pdf','w')
arquivo.write(report_data)
    