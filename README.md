This documentation is for the use for the use of the REST api connected to piggybank app

Create God (NOTE: This ID is no longer available since the DELETE function was called)
	type: PUT
	function name: god
	parameters: username, password
	description: Hashes the password to use as the god_id, and saves the username as a global secondary index. Both of these can be searched in the database to retrieve the account. A god account is created with these parameters
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god?password=test&username=mason"
			"$pbkdf2-sha256$500002$DYFw7h0jZMyZE2JszVlLqQ$VXJkjywoOpxLbDmeB62iXnML1NmHf92.Bprmj9wtjds"
				
Get God (NOTE: This ID is no longer available since the DELETE function was called)
	type: GET
	function name: god
	parameters: god_id
	description: Uses a god_id to retrieve the god account attributed to that id
	errors: Returns -1 if there is no account attributed to that id
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god?god_id=$pbkdf2-sha256$500002$DYFw7h0jZMyZE2JszVlLqQ$VXJkjywoOpxLbDmeB62iXnML1NmHf92.Bprmj9wtjds"
			{"username": "mason", "guardian": {}, "accounts": {}, "child_count": 0, "god": {"log": []}, "avail_child": [], "god_id": "$pbkdf2-sha256$500002$DYFw7h0jZMyZE2JszVlLqQ$VXJkjywoOpxLbDmeB62iXnML1NmHf92.Bprmj9wtjds", "children": {}}

Delete God (NOTE: This ID is no longer available since the DELETE function was called)
	type: DELETE
	function name: god
	parameters: god_id
	description: Uses a god_id to delete the account attributed to that id. Returns 0 on successful operation
	errors: Returns -1 if there is no account attributed to that id
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god?god_id=$pbkdf2-sha256$500002$DYFw7h0jZMyZE2JszVlLqQ$VXJkjywoOpxLbDmeB62iXnML1NmHf92.Bprmj9wtjds" 
			0

Get God ID
	type: GET
	function name: god/godid
	parameters: username,password
	description: Uses the username to search for the account. Takes the hash attributed to that username, and then verifies the password with the god_id. If it matches, the god_id is returned
	errors: Returns -1 if the username does not match to an account, or if the password is incorrect
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god/godid?username=mason&password=test"
			"$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4"

Put God Name (NOTE: Using '_' or '+' or '-' etc to represent spaces is totally up to you)
	type: PUT
	function name: god/godname
	parameters: god_id,god_name
	description: Adds/Changes the name associated with the god account. Returns 0 on successful operation
	errors: Returns -1 if the god_id does not match to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god/godname?god_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4&god_name=Mason_Bruce"
			0

Get God Name
	type: GET
	function name: god/godname
	parameters: god_id
	description: Uses a god_id to return the name attributed to that account. 
	errors: returns -1 if the god_id does not match to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god/godname?god_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4"
			"Mason_Bruce"

Put God Pic
	type: PUT
	function name: god/godpic
	parameters: god_id,god_pic
	description: Adds/Changes the picture name associated with the god account. Returns 0 on successful operation
	errors: Returns -1 if the god_id does not match to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god/godpic?god_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4&god_pic=default.jpg"
			0

Get God Pic
	type: GET
	function name: god/godpic
	parameters: god_id
	description: Uses a god_id to return the name attributed to that account
	errors: returns -1 if the god_id does not match to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god/godpic?god_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4"
			"default.jpg"

Create Guardian (NOTE: Requires that the guardian NAME and PIC already be set. Kind of annoying for testing purposes, but in reality this information will be readily available on account creation)
	type: PUT
	function name: guardian
	parameters: god_id, guardian_id
	description: Uses a god_id and guardian_id to create a guardian. The guardian is saved to the god account, and the god_account and permission 'guardian' is saved to the guardian account
	errors: returns -1 if the god_id does not match to an account or if the guardian_id does not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/guardian?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&guardian_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4"
			0

Get Guardian
	type: GET
	function name: guardian
	parameters: god_id,guardian_id
	description: Uses a god_id and guardian_id to find the guardian account. Returns the guardian
	errors: returns -1 if the god_id does not match to an account or if the guardian_id does not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/guardian?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&guardian_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4"
			{"guardian_pic": "default.jpg", "guardian_name": "Mason_Bruce"}

Delete Guardian
	type: DELETE
	function name: guardian
	parameters: god_id,guardian_id
	description: Uses a god_id and a guardian_id to find the guardian account. Deletes the guardian
	errors: returns -1 if the god_id does not match to an account or if the guardian_id does not match up to an account
	example:
			