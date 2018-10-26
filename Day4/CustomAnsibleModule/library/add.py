from ansible.module_utils.basic import AnsibleModule

def add(val1,val2):
    return val1+val2

def main():
    module = AnsibleModule (
	argument_spec = dict (
		firstValue = dict( type='float', required='True'),
		secondValue = dict( type='float', required='True')
	)
    )

    val1 = module.params['firstValue']
    val2 = module.params['secondValue']

    result = add(val1,val2)

    #The below code must be used in case everything worked fine - success path
    module.exit_json( meta=result, changed=True, rc=0 )
    
    #The below function must be invoked to indicate an error - failure path
    #module.fail_json( msg="Fatal error" )

main()




