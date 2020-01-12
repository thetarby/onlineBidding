import React from 'react';
export default class MyProfile extends React.Component { 
    constructor(props){
        super(props)
        this.state = {}
        this.addBalance = this.addBalance.bind(this)
        this.changePassword = this.changePassword.bind(this)
        this.watchItemType=this.watchItemType.bind(this)
    }


    componentWillMount(){
        var request = new Request(
            'http://localhost:8000/profile/',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var data = {
            csrfmiddlewaretoken:this.getCookie('csrftoken')
        };
        var thisOfClass=this;
        fetch(request, {
            method: 'POST',
            mode: 'same-origin',  // Do not send CSRF token to another domain.
            body: JSON.stringify(data)
        }).then(function(response) {
            return (response.json())
        }).then(function(json){
            console.log(json)
            thisOfClass.setState({
                "name_surname": json.data.name_surname, 
                "email": json.data.email,
                "balance": json.data.balance
            })
        })
    }

    addBalance(){
        var request = new Request(
            'http://localhost:8000/home/add_balance/',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var added_amount = document.getElementById('amount-value').value;
        var data = {
            amount: added_amount,
            csrfmiddlewaretoken:this.getCookie('csrftoken')
        };
        var thisOfClass=this;
        fetch(request, {
            method: 'POST',
            mode: 'same-origin',  // Do not send CSRF token to another domain.
            body: JSON.stringify(data)
        }).then(function(response) {
            return (response.json())
        }).then(function(json){
            if (json['result'] == 'Success'){
                thisOfClass.setState({
                    "name_surname": json.data.name_surname, 
                    "email": json.data.email,
                    "balance": json.data.balance
<<<<<<< HEAD
                })
            }
                
        });
=======
            })
        })



        var request = new Request(
            'http://localhost:8000/bid/user-history/',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var data = {
            csrfmiddlewaretoken:this.getCookie('csrftoken')
        };
        var thisOfClass=this;
        fetch(request, {
            method: 'POST',
            mode: 'same-origin',  // Do not send CSRF token to another domain.
            body: JSON.stringify(data)
        }).then(function(response) {
            return (response.json())
        }).then(function(json){
            console.log('!!!!!!!!!!! history',json)
            thisOfClass.setState({hist:json.data})
        })
    }
    watchItemType(){
        var request = new Request(
            'http://localhost:8000/bid/watch-item-type/'+document.getElementById('item-type-watch').value
        );
        var thisOfClass=this;
        fetch(request, {
            method: 'GET',
        }).then(function(response) {
            return (response.json())
        })
>>>>>>> f6e6e390bfddd62cb4a7e97cb9a9208d7dbb74d8
    }

    changePassword(){
        var request = new Request(
            'http://localhost:8000/home/change_password/',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var data = {
            old_password: document.getElementById('old-password').value,
            new_password: document.getElementById('new-password').value,
            csrfmiddlewaretoken:this.getCookie('csrftoken')
        };
        var thisOfClass=this;
        fetch(request, {
            method: 'POST',
            mode: 'same-origin',  // Do not send CSRF token to another domain.
            body: JSON.stringify(data)
        }).then(function(response) {
            return response.json()
        }).then(function(json){
            if (json['result'] == 'Success'){
                console.log('SUCCESS')
                thisOfClass.setState({
                    "change_password_message": "Password is changed successfully"
                })
            }
            else {
                console.log('FAIL')
                thisOfClass.setState({
                    "change_password_message": "Password is incorrect"
                })
            }
                
        });
    }

    getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = (cookies[i]).trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

	render(){
		return(
			<div>
                <p> Ad Soyad: { this.state.name_surname }</p>
                <p> Email: { this.state.email }</p>
                <p> Bakiye: { this.state.balance }</p>
                <hr></hr>
                <input class="form-control" type={"text"} id='amount-value' name={"amount"} placeholder={"0"}></input>
                <button onClick={this.addBalance}>Add Balance</button>
                <hr></hr>
                <input type="password" class="form-control" id="old-password" placeholder="Old Password"></input>
                <input type="password" class="form-control" id="new-password" placeholder="New Password"></input>
                <button onClick={this.changePassword}>Change Password</button>
                {
                    this.state.change_password_message ?
                    <p>{this.state.change_password_message}</p>:
                    null
                }

                <input type={"text"} name={"item_type"} placeholder={"item type to watch"} id={'item-type-watch'}></input>
                <button onClick={this.watchItemType}>Submit</button>

                <p>sold:</p>
                
                {
                    this.state.hist ? this.state.hist.owned_sells.map(d=> <div style={{background:'red', margin:'20px', padding:'10px;'}}><p>item: {d.item.title}</p><p>sold price: {d.current_price}</p></div> ) : ""
                }

                <p>won:</p>
                {
                    this.state.hist ? this.state.hist.won_sellls.map(d=>  <div style={{background:'red', margin:'20px', padding:'10px;'}}><p>item: {d.item.title}</p><p>paid price: {d.current_price}</p></div> ) : ""
                }
            </div>
			);
	}
}