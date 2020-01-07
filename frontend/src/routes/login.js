import React from 'react';
export default class Login extends React.Component { 

	render(){
		return(
			<div>
                <form action={"http://localhost:8000/login/"} method={"POST"}>
                <input type={"hidden"} name={"csrfmiddlewaretoken"} value={"04u7yDfpc7ft1AihRexxw7X9zBl0VoTx4eibcCojXjOo3x4l4douo6Ub8KdXwGli"}></input>
                <fieldset className={"form-group"}>
                    <legend className={"border-bottom mb-4"}>Log In</legend>
                    <label for={"id_username"}>Username:</label><input type={"text"} name={"username"} autofocus={""} autocapitalize={"none"} autocomplete={"username"} maxlength={"150"} required={""} id={"id_username"}></input>
                    <label for={"id_password"}>Password:</label><input type={"password"} name={"password"} autocomplete={"current-password"} required={""} id={"id_password"}></input>
                </fieldset>
                <div className={"form-group"}>
                    <input type={"submit"} value={"Log In!"}></input>
                </div>
                </form>
            </div>
			);
	}
}