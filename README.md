# This documentation is for the use for the use of the REST api connected to piggybank app

##### NOTE: errors being -1 or key error are almost always equivalent 


**Create God (NOTE: This ID is no longer available since the DELETE function was called)**
- type: PUT
- function name: god
- parameters: username, password
- description: Hashes the password to use as the god_id, and saves the username as a global secondary index. Both of these can be searched in the database to retrieve the account. A god account is created with these parameters
- example:
>curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god?password=test&username=mason"
	
	>"$pbkdf2-sha256$500002$DYFw7h0jZMyZE2JszVlLqQ$VXJkjywoOpxLbDmeB62iXnML1NmHf92.Bprmj9wtjds"
				
**Get God (NOTE: This ID is no longer available since the DELETE function was called)**
-type: GET
-function name: god
-parameters: god_id
-description: Uses a god_id to retrieve the god account attributed to that id
-errors: Returns -1 if there is no account attributed to that id
-example:
>curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god?god_id=$pbkdf2-sha256$500002$DYFw7h0jZMyZE2JszVlLqQ$VXJkjywoOpxLbDmeB62iXnML1NmHf92.Bprmj9wtjds"

	>{"username": "mason", "guardian": {}, "accounts": {}, "child_count": 0, "god": {"log": []}, "avail_child": [], "god_id": "$pbkdf2-sha256$500002$DYFw7h0jZMyZE2JszVlLqQ$VXJkjywoOpxLbDmeB62iXnML1NmHf92.Bprmj9wtjds", "children": {}}

**Delete God (NOTE: This ID is no longer available since the DELETE function was called)**
-type: DELETE
-function name: god
-parameters: god_id
-description: Uses a god_id to delete the account attributed to that id. Returns 0 on successful operation
-errors: Returns -1 if there is no account attributed to that id
-example:
	>curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/god?god_id=$pbkdf2-sha256$500002$DYFw7h0jZMyZE2JszVlLqQ$VXJkjywoOpxLbDmeB62iXnML1NmHf92.Bprmj9wtjds" 
	>0

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

Put log (NOTE: Messages with the same name are still appended to the list, but with different times. This list does not exist anymore since DELETE was called on it)
	type: PUT
	function name: log
	parameters: god_id,message
	description: Appends the message with the current time to the god account
	errors: returns -1 if the god_id does not match to an account. Errors out if the message is an empty string
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/log?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&message=Chore:Wash_The_Dishes__Confirmed"
			0
Delete log (NOTE: can be changed to removing based on time or index in the list later if needed)
	type: DELETE
	function name: log
	parameters: god_id,message
	description: Find the message on the god log by name, and removes it from the list. Removes the first occurrence of the name, duplicate messages will NOT be deleted with one function call
	errors: returns -1 if the god_id does not match to an account, or if the given message can not be found
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/log?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&message=Chore:Wash_The_Dishes__Confirmed"
			0
Get log list (NOTE: This list does not exist anymore since DELETE was called on it)
	type: GET
	function name: log/logall
	parameters: god_id
	description: Returns the entire log attributed to the god account
	errors: returns -1 if the god_id does not match to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/log/logall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk"
			[{"message": "Chore:Wash_The_Dishes__Confirmed", "time": "2017-11-14 04:42:14.238550"}, {"message": "Chore:Wash_The_Dishes__Confirmed", "time": "2017-11-14 04:42:23.597436"}]

Delete log list
	type: DELETE
	function name: log/logall
	parameters: god_id
	description: Deletes the entire log attributed to the god account. Returns 0 on successful operation
	errors: returns -1 if the god_id does not match to an account
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/log/logall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk"
			0
			
Create Guardian (NOTE: Requires that the guardian NAME and PIC already be set. Kind of annoying for testing purposes, but in reality this information will be readily available on account creation.)
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
	description: Uses a god_id and a guardian_id to find the guardian account. Deletes the guardian. Returns 0 on successful operation.
	errors: returns -1 if the god_id does not match to an account or if the guardian_id does not match up to an account
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/guardian?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&guardian_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4"
			0

NOTE: THESE NEXT 4 FUNCTIONS ONLY CHANGE THE NAME AND PIC ON THE GOD ACCOUNT. NOT THE GUARDIAN'S GOD ACCOUNT
	EX: Guardian Name saved to Guardian's God Account: Darren Atkinson
		Mason(child) refers to Guardian as Big Daddy Adi, so Guardian Name shown to the child is Big Daddy Adi

Put Guardian Name (NOTE: This only changes the guardian name on the GOD account, not the guardian name on the guardian account. You can just not use this function, or use it to save nicknames on the GOD account. If you want to change the Guardian name on their own account and the name on the GOD account, you must call both functions)
	type: PUT
	function name: guardian/guardianname
	parameters: god_id,guardian_id,guardian_name
	description: Sets/Changes the guardian name on the god account. Does not affect the guardian name on their own god account. Returns 0 on successful operation
	errors: returns -1 if the god_id or the guardian_id do not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/guardian/guardianname?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&guardian_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4&guardian_name=Mickey_Huang"
			0

Get Guardian Name (NOTE: This gets the guardian name on the god account)
	type: GET
	function name: guardian/guardianname
	parameters: god_id,guardian_id
	description: Returns the guardian name attributed to the god account
	errors: returns -1 if the god_id or guardian_id do not match up to an account 
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/guardian/guardianname?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&guardian_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4"
			"Mickey_Huang"

Put Guardian Pic (NOTE: This only changes the guardian pic on the GOD account, not the guardian name on the guardian account. You can just not use this function, or use it to save a different pic on the GOD account. If you want to change the Guardian pic on their own account and the name on the GOD account, you must call both functions)
	type: GET
	function name: guardian/guardianpic
	parameters: god_id,guardian_id,guardian_pic
	description: Sets/Changes the guardian pic on the god account. Does not acffect the guardian pic on their own god account. Returns 0 on successful operation
	errors: returs -1 if the god_id or guardian_id do not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/guardian/guardianpic?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&guardian_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4&guardian_pic=default.jpg"
			0

Get Guardian Pic (NOTE: This gets the guardian name on the god account)
	type: GET
	function name: guardian/guardianpic
	parameters: god_id,guardian_id
	description: Returns the guardian pic attributed to the guardian account
	errors: returns -1 if the god_id or guardian_id do not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/guardian/guardianpic?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&guardian_id=$pbkdf2-sha256$500002$vrfWeq.11vpfq/XeGyNkrA$GTO9XIcTKYWt1ren2MTQ2Biku9Dd9bJDxHM.VPfKja4"
			"default.jpg"

Create Child
	type: PUT
	function name: child
	parameters: god_id
	description: Creates a child account under the god account, and then returns the child ID
	errors: returns -1 if the god_id does not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk"
			0

Get Child
	type: GET
	function name: child
	parameters: god_id,child_id
	description: Returns the child account given by the child ID
	errors: returns -1 if the god_id does not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			{"achievements": [], "chore": [], "log": [], "wish": [], "points": 0, "permissions": {"pic": 1, "name": 1}}

Delete Child
	type: DELETE
	function name: child
	parameters: god_id,child_id
	description: Deletes the child account. Returns 0 on successful operation
	errors: returns -1 if the child_id or god_id do not match up to an account
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			0

Get Child List
	type: GET
	function name: child/childall
	parameters: god_id
	description: Returns all child accounts attributed to the god_id
	errors: returns -1 if the god_id does not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk"
			{"1": {"achievements": [], "chore": [], "log": [], "wish": [], "points": 0, "permissions": {"pic": 1, "name": 1}}, "0": {"achievements": [], "chore": [], "log": [], "wish": [], "points": 0, "permissions": {"pic": 1, "name": 1}}, "2": {"achievements": [], "chore": [], "log": [], "wish": [], "points": 0, "permissions": {"pic": 1, "name": 1}}}

Put Child Log
	type: PUT
	function name: child/childlog
	parameters: god_id,child_id,message
	description: Adds the given message to the child account with the current time. Returns 0 on successful operation.
	errors: Returns -1 if the god_id or child_id does not natch up to an account. Errors out if message is an empty string
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childlog?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&message=Chore__Wash_The_Wishes_Completed"
			0

Delete Child Log (NOTE: Deletes the first message in the list that matches the given message)
	type: Delete
	function name:child/childlog
	parameters: god_id,child_id,message
	description: Searches the entire child log for the message with the same name as given, and then deletes it from the list. Returns 0 on successful operation.
	errors: Returns -1 if the god_id or child_id does not match up to an account. Errors out if the message is an empty string
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childlog?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&message=Chore__Wash_The_Wishes_Completed"
			0

Get Child Log All
	type: GET
	function name: child/childlog/childlogall
	parameters: god_id,child_id
	description: Returns the entire child log
	errors: returns -1 if the god_id or child_id does not match up to an account.
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childlog/childlogall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			[{"message": "Chore__Wash_The_Wishes_Completed", "time": "2017-11-15 01:16:41.253299"}, {"message": "Chore__Wash_The_Wishes_Completed", "time": "2017-11-15 01:16:43.311125"}, {"message": "Chore__Wash_The_Wishes_Completed", "time": "2017-11-15 01:16:44.891473"}]

Delete Child Log All
	type: DELETE
	function name: child/childlog/childlogall
	parameters: god_id,child_id
	description: Deletes the entire child log list. Returns 0 on successful operation
	errors: returns -1 if the god_id or child_id does not match up to an account
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childlog/childlogall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			0

Put Child Name
	type: PUT
	function name: child/childname
	parameters: god_id,child_id,child_name,permission
	description: Adds/Changes the name of the given child. (permission = 0, read privileges, permission = 1+ write privileges) Returns 0 on successful operation
	errors: returns -1 if the god_id or child_id does not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childname?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&permission=1&child_name=Zachary"
			0

Get Child Name
	type: GET
	function name: child/childname
	parameters: god_id,child_id
	description: Returns the child name attributed to the given child
	errors: returns -1 if the god_id or the child_id does not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childname?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			"Zachary"

Get Child Permissions
	type: GET
	function name: child/childperm
	parameters: god_id,child_id
	description: Returns the permissions atributted to the given child
	errors: returns -1 if the god_id or child_id does not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childperm?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			{"pic": 1, "name": 1}

Put Child Name Permission
	type: PUT
	function name: child/childperm/childnameperm
	parameters: god_id,child_id,name_lvl,permission
	description: Changes the name permissions of the child. name_lvl is the child permission level to change. Permission is the permission lvl of guardian/god. permission = 1+ write privileges, permission = 0 error. Returns 0 on successful operation
	error: returns -1 if the god_id or child_id does not match up to an account, or if the permission lvl is 0 (less than 1)
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childperm/childnameperm?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&permission=1&name_lvl=0"
			0

Put Child Pic Permission
	type: PUT
	function name: child/childperm/childpicperm
	parameters: god_id,child_id,pic_lvl,permission
	description: Changes the pic permissions of the child. pic_lvl is the child permission level to change. Permission is the permission lvl of guardian/god. permission = 1+ write priveleges, permission = 0, error. Returns 0 on successful operation
	errors: returns -1 if the god_id or child_id does not match up to an account, or if the permission lvl is 0 (less than 1)
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childperm/childpicperm?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&permission=1&pic_lvl=0"
			0

Put Child Pic
	type: PUT
	function name: child/childpic
	parameters: god_id,child_id,permission
	description: Adds/Changes the pic of the given child. Permission is the permission lvl of guardian/god. (permission = 0, read privilges, permission = 1+ write privileges) Returns 0 on successful operation
	errors: returns 1- if the god_id or child_id does not match up to an account, or if the permission lvl is 0 (less than 1)
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childpic?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&permission=1&child_pic=default.jpg"
			0

Get Child Pic
	type: GET
	function name: child/childpic
	parameters: god_id,child_id
	description: Returns the pic attributed to the given child
	errors: returns -1 if the god_id or child_id does not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/childpic?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			"default.jpg"

Add Points (NOTE: I can change this to return the current balance if that's more helpful)
	type: PUT
	function name: child/points
	parameters: god_id,child_id,message,amount,permission
	description: Adds the amount to the total amount of points that the child has. The message is optional, with no message being notated by "NULL". Permission is the permission lvl of guardian/god. permission = 1+ write priveleges, permission = 0, error. Returns 0 on successful operation.
	errors: returns -1 if the god_id or child_id does not match up to an account, or if the permission lvl is 0 (less than 1)
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/points?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&permission=1&amount=10000&message=Bonus_Prize"
			0

Delete Points (Note: I can change this to return the current balance if that's more helpful)
	type: DELETE
	function name: child/points
	parameters: god_id,child_id.message,amount,permission
	description:  Removes the amount to the total amount of points that the child has. The message is optional, with no message being notated by "NULL". Permission is the permission lvl of guardian/god. permission = 1+ write priveleges, permission = 0, error. Returns 0 on successful operation.
	errors:	returns -1 if the god_id or child_id does not match up to an account, or if the permission lvl is 0 (less than 1)
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/points?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&permission=1&amount=5000&message=Punishment_-5000"
			0

Get Points
	type: GET
	function name: child/points
	parameters: god_id,child_id
	description: Returns the total amount of points that the child has.
	errors: returns -1 if the god-id or child_id does not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/child/points?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			5000

Put Chore
	type: PUT
	function name: chore
	parameters: god_id,child_id,chore_name,interval,day_reset,time_reset,reward,pic
	description: Creates a chore for a child
				 NOTE: These values are suggestions, and are completely up to you to add and interpret
				 interval = how often the chore resets (1 - ...) 0 = No reset aka 1 time chore. 
				 NOTE: Day reset must change constantly if the interval is not 1 week
				 EX: interval = 1 (chore resets ever day)
				 day_reset = 1 (Sunday)
				 Once the chore is completed on Sunday, the day_reset changes to (day_reset + interval)%7 (Logic not programmed in server side)
					
				 day_reset = the day that the chore resets (1 = Sunday, ... , 7 = Saturday) 0 = no reset aka 1 time chore
				 time_reset = the time that the chore resets (any time format you want, I can change to one variable time/date but i thought this would be easier to edit) -1 = no reset aka 1 time chore
				 reward = the amount of points added when the chore is complete
				 This function doesn't do any of the logic for adding points server side, so using these variables to add points should be done client side, unless you want me to add the logic serverside, would have to create a new function choreUpdate() or something similar for u to call to use it, but the logic can be done client side so i didnt think i needed it
				 returns 0 on successful operation
	errors: returns -1 if the god_id or child_id does not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Wash_The_Dishes&interval=1&day_reset=1&time_reset=1300&reward=100&pic=dishes.jpg"
			0

Get Chore (NOTE: I can change the 3rd parameter to be whatever you want, as long as its searchable)
	type: GET
	function name: chore
	parameters: god_id, child_id,chore_name
	description: returns the chore specified by the name
	errors: returns -1 if the god_id or child_id does not match up to an account, or if the chore with the chore_name does not exist
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Wash_The_Dishes"
			{"day_reset": 1, "confirm": 0, "pic": "dishes.jpg", "time_reset": 1300, "interval": 1, "chore_name": "Wash_The_Dishes", "reward": 100}

Delete Chore
	type: DELETE
	function name: chore
	parameters: god_id,child_id,chore_name
	description: deletes the chore specified by the name, returns 0 on successful operation
	errors: returns -1 if the god_id or child_id does not match up to an account, or if the chore with the chore_name does not exist
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Wash_The_Dishes"
			0

Get Chore List
	type: GET
	function name: chore/choreall
	parameters: god_id,child_id
	description: returns the entire chore list
	errors: returns -1 if the god_id or child_id do not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/choreall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			[{"day_reset": 1, "confirm": 0, "pic": "dishes.jpg", "time_reset": 1300, "interval": 1, "chore_name": "Wash_The_Dishes", "reward": 100}, {"day_reset": 1, "confirm": 0, "pic": "dishes.jpg", "time_reset": 1300, "interval": 1, "chore_name": "Wash_The_Dishes", "reward": 100}, {"day_reset": 1, "confirm": 0, "pic": "dishes.jpg", "time_reset": 1300, "interval": 1, "chore_name": "Wash_The_Dishes", "reward": 100}]

Delete Chore List
	type: DELETE
	function name: chore/choreall
	parameters: god_id,child_id
	description: Deletes the entire chore list, returns 0 on successful operation
	errors: returns -1 if the god_id or child_id do not match up to an account
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/choreall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			0

Put Chore Confirm
	type: PUT
	function name: chore/choreconfirm
	parameters: god_id,child_id,chore_name,confirm
	description: Changes the confirm number to the given value (NOTE: Can also be used to unconfirm since the value does not matter. Not Confirmed = 0 and Confirmed = 1) returns 0 on successful operation
		No permission requiered since whats the point of a guardian that can't confirm chores
	errors: returns -1 if the god_id, or child_id do not match up to an account, or if the chore_name does not match any chores
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/choreconfirm?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Wash_The_Dishes&confirm=1"
			0

Put Chore Day (NOTE: No Permissions yet, but I can add it later when we work out all the details on what needs permissions and what doesn't)
	type: PUT
	function name: chore/choreday
	parameters: god_id,child_id,chore_name,day_reset
	description: Changes the day_reset to the given value. returns 0 on successful operation
	errors: returns -1 if the god_id, or child_id do not match up to an account, or if the chore_name does not exist
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/choreday?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Wash_The_Dishes&day_reset=1"
			0

Put Chore Interval (NOTE: No Permissions yet, but I can add it later when we work out all the details on what needs permissions and what doesn't)
	type: PUT
	function name: chore/choreinterval
	parameters: god_id,child_id,chore_name,interval
	description: Changes the chore interval to the given value. returns 0 on successful operation
	errors: returns -1 if the god_id or child_id do not match up to an account, or if the chore_name does not exist
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/choreinterval?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Wash_The_Dishes&interval=1"
			0

Put Chore Name (NOTE: No Permissions yet, but I can add it later when we work out all the details on what needs permissions and what doesn't)
	type: PUT
	function name: chore/chorename
	parameters: god_id,child_id,chore_name,new_name
	description: changes the chore name to the new name. returns 0 on successful operation 
	errors: returns -1 if the god_id or child_id do not match up to an account, or if the chore_name does not exist
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/chorename?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Wash_The_Dishes&new_name=Clean_Dishes"
			0

Put Chore Pic (NOTE: No Permissions yet, but I can add it later when we work out all the details on what needs permissions and what doesn't)
	type: PUT
	function name: chore/chorepic
	parameters: god_id,child_id,chore_name,pic
	description: changes the chore pic to the new pic. returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account, or if the chore_name does not exist
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/chorepic?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Clean_Dishes&pic=default2.jpg"
			0

Put Chore Reward
	type: PUT
	function name: chore/chorereward
	parameters: god_id,child_id,chore_name,reward
	description: changes the chore reward to the given value. returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account, or if the chore_name does not exist
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/chorereward?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Clean_Dishes&reward=1000"
			0

Put Chore Time_Reset
	type: PUT
	function name: chore/choretime
	parameters: god_id,child_id,chore_name,time_reset
	description: changes the chore time_reset to the given value. returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account, or if the chore_name does not exist
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/chore/choretime?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&chore_name=Clean_Dishes&time_reset=1000"
			0

Put Wish
	type: PUT
	function name: wish
	parameters: god_id,child_id,wish_name,pic
	description: Adds a wish to the list. Returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&wish_name=Bike&pic=bike.jpg"
			0

Get Wish (NOTE: None of the logic for using this information is implemented server side)
	type: GET
	function name: wish
	parameters: god_id,child_id,wish_name
	description: Returns the wish specified by the name
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&wish_name=Bike"
			{"wish_name": "Bike", "cost": 0, "pic": "bike.jpg", "confirm": 0}

Delete Wish
	type: DELETE
	function name: wish
	parameters: god_id,child_id,wish_name,permission
	description: deletes the wish specified by the name, returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&wish_name=Bike&permission=1"
			0

Get Wish List
	type: GET
	function name: wish/wishall
	parameters: god_id,child_id
	description: Returns the entire wishlist
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X GET "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish/wishall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"			
			[{"wish_name": "Bike", "cost": 0, "pic": "bike.jpg", "confirm": 0}, {"wish_name": "Bike", "cost": 0, "pic": "bike.jpg", "confirm": 0}]

Delete Wish List
	type: GET
	function name: wish/wishall
	parameters: god_id,child_id
	description: Deletes the entire wish list. returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X DELETE "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish/wishall?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0"
			0

Wish Confirm
	type: PUT
	function name: wish/wishconfirm
	parameters: god_id,child_id,wish_name,confirm,permission
	description: Changes the confirm number to the given value
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish/wishconfirm?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&wish_name=Bike&confirm=1&permission=1"
			0

Wish Cost
	type: PUT
	function name: wish/wishcost
	parameters: god_id,child_id,wish_name,cost,permission
	description: Adds/Changes the cost for the given wish. returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish/wishcost?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&wish_name=Bike&cost=1000&permission=1"
			0

Wish Name
	type: PUT
	function name: wish/wishname
	parameters: god_id,child_id,wish_name,new_name,permission
	description: Changes the name for the given wish. returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish/wishname?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&wish_name=Bike&new_name=Speed_Racer&permission=1"
			0

Wish Pic
	type: PUT
	function name: wish/wishpic
	parameters: god_id,child_id,wish_name,pic,permission
	description: Changes the picture for the given wish. returns 0 on successful operation
	errors: returns -1 if the god_id or the child_id do not match up to an account
	example:
			curl -X PUT "https://60y6l6qi3c.execute-api.us-west-1.amazonaws.com/alpha/wish/wishpic?god_id=$pbkdf2-sha256$500002$xdj739vb.z/HmJMSQuhdyw$EpJzuydLRzCUN5ei8BbvCJOfUk0AYYeI.jm7uIzHgUk&child_id=0&wish_name=Speed_Racer&pic=default4.jpg&permission=1"
			0
			
