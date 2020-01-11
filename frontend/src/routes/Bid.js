import React from 'react';
import './bid.css';
import axios from 'axios'
export default class Bid extends React.Component {
    constructor(props){
        super(props)
        this.state={
            selected_item_id:'',
            sells:[
                {
                    'item':{
                        'id':"1",
                        "title":"Iphone X",
                        "owner":{
                            "name_surname":"Furkan Akyol",
                        },
                        "item_type":"Phone",
                        "description":"Çiziksiz süper ikinci el telefon"
                    },
                    'current_price':"10",

                },
                {
                    'item':{
                        'id':"2",
                        "title":"Mercedes C Coupe",
                        "owner":{
                            "name_surname":"Azad Baykara",
                        },
                        "item_type":"Car",
                        "description":"100.000 kmde doktordan az kullanılmış"
                    },
                    'current_price':"300.000",

                }
            ]
        }
        this.getData = this.getData.bind(this);
    }

    componentWillMount(){
        this.getData()
        let counter = setInterval(this.getData, 1000);

    }

    getData() {
        // create a new XMLHttpRequest
        var xhr = new XMLHttpRequest()

        // get a callback when the server responds
        xhr.addEventListener('load', () => {
          // update the state of the component with the result here
          this.setState({sells:JSON.parse(xhr.responseText)['data']})
        })
        // open the request with the verb and the url
        xhr.open('GET', 'http://localhost:8000/bid/test/')
        // send the request
        xhr.send()
    }
    watchItem(item_id){
        var request = new Request(
            'http://localhost:8000/bid/watch-sell/',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var data = {
            csrfmiddlewaretoken:this.getCookie('csrftoken'),
            item_id:item_id
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
        })
    }
    sendBidReq(){
        var request = new Request(
            'http://localhost:8000/bid/bidding/1',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var data = {
            csrfmiddlewaretoken:this.getCookie('csrftoken')
        };
        var el=document.getElementById('form-send-bid')
        var htmlCol=el.children
        for(var i=1; i<htmlCol.length-1;i++){
            data[htmlCol[i].name]=htmlCol[i].value
        }
        var thisOfClass=this;
        fetch(request, {
            method: 'POST',
            mode: 'same-origin',  // Do not send CSRF token to another domain.
            body: JSON.stringify(data)
        }).then(function(response) {
            return (response.json())
        }).then(function(json){
            console.log(json)
        })

    }
    clickHandler(e){
        console.log(e)
        if(e==='bid'){
            this.sendBidReq()
        }
        else if(e.target.className==='fa fa-bell'){
            this.watchItem(e.currentTarget.id)
            console.log('dasdjkas')
        }
        else{
            this.setState({selected_item_id:e.currentTarget.id})
        }
    }
    getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    render(){
        if(this.state.selected_item_id==''){
            return (
                <div>
                    <h1>Current Auctions:</h1>
                    {
                        this.state.sells.map((sell)=>
                            <div onClick={(e)=>this.clickHandler(e)} id={sell.id} className={"card"}>
                                <div className={"additional"}>
                                    <div className={"item-image"}>
                                        <i className={"fa fa-bell"}></i>

                                        <img src={"https://www.dhresource.com/600x600/f2/albu/g7/M01/D3/91/rBVaSVrsd5aAA5isAAMVt25ugBc771.jpg"} alt={"Item Photo"}></img>
                                        <div className={"item-price"}>
                                            {sell.current_price}₺
                                        </div>
                                    </div>
                                </div>
                                <div className={"general"}>
                                    <div className={"item-info"}>
                                        <p className={"left"}> Owner: { sell.item.owner.name_surname }</p>
                                        <p className={"right"}>Type: { sell.item.item_type }</p>
                                    </div>
                                    <h1>{ sell.item.title }</h1>
                                    <p>{ sell.item.description }</p>
                                    <span>Click On Item to Go Auction Page</span>
                                </div>
    
                            </div>
                        )
                    }
                    
                </div>
              );
        }
        else{
            var sell=this.state.sells.filter((d)=> d.id==this.state.selected_item_id)[0]
            var csrftoken = this.getCookie('csrftoken');
            return(
                <div>
                    <button onClick={()=>this.setState({selected_item_id:''})}>all items</button>
                    <div style={{margin:"50px", border:"1px solid", width: "300px"}}>
                        <p>{ sell.item.title }</p>
                        <p>{sell.item.description}</p>
                        <p>{sell.item.item_type}</p>
                        <p>{sell.current_price}</p>
                        { /* {% csrf_token %} */ }
                        <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
                        <fieldset id='form-send-bid' className={"form-group"}>
                            <legend className={"border-bottom mb-4"}>Make A Bid</legend>
                            <input type={"text"} name={"amount"} placeholder={"0"}></input>
                            <input type={"hidden"} name={"item_id"} value={sell.item.id}></input>
                            <button className="btn" onClick={()=>this.clickHandler('bid')}>Bid!</button>
                        </fieldset>
                    </div>


<div className='bid_form' id="login-box">
  <div className="left">
    <h1>Sign up</h1>
    
    <input type="text" name="username" placeholder="Username" />
    <input type="text" name="email" placeholder="E-mail" />
    <input type="password" name="password" placeholder="Password" />
    <input type="password" name="password2" placeholder="Retype password" />
    
    <input type="submit" name="signup_submit" value="Sign me up" />
  </div>
  
  <div className="right">
    <span className="loginwith">Sign in with<br />social network</span>
    
    <button className="social-signin facebook">Log in with facebook</button>
    <button className="social-signin twitter">Log in with Twitter</button>
    <button className="social-signin google">Log in with Google+</button>
  </div>
  <div className="or">OR</div>
</div>
                </div>
            );
        }
    }

}
