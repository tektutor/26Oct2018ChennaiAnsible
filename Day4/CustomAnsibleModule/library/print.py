from ansible.module_utils.basic import AnsibleModule

def printMessage(msg):
    print(msg)
    return msg

def main():
    module = AnsibleModule (
	argument_spec = dict (
		msg = dict( type='str', required='True')
	)
    )

    msg = module.params['msg']
   
    response = printMessage(msg)

    #The below code must be used in case everything worked fine - success path
    module.exit_json( meta=response, changed=False, rc=0 )
    
    #The below function must be invoked to indicate an error - failure path
    #module.fail_json( msg="Fatal error" )

main()




