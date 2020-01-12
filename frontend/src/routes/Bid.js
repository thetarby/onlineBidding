import React from 'react';
import './bid.css';
import axios from 'axios'
import Chart from "react-apexcharts";

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
            ],
            history:[]
        }
        this.getData = this.getData.bind(this);
    }

    componentWillMount(){
        this.getData()
        console.log('compenent will mount')
        this.counter = setInterval(this.getData, 1000);

    }

    getData() {
        if(this.state.selected_item_id==""){
            // create a new XMLHttpRequest
            var xhr = new XMLHttpRequest()

            // get a callback when the server responds
            xhr.addEventListener('load', () => {
            // update the state of the component with the result here
            if (JSON.parse(xhr.responseText)['data'].filter((d)=> this.state.selected_item_id==d.id).length==0) this.setState({selected_item_id:'', sells:JSON.parse(xhr.responseText)['data']})
            else this.setState({sells:JSON.parse(xhr.responseText)['data']})

            })
            // open the request with the verb and the url
            xhr.open('GET', 'http://localhost:8000/bid/test/')
            // send the request
            xhr.send()
        }
        else{
            var request = new Request(
                'http://localhost:8000/bid/asd/'+this.state.selected_item_id,
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
                console.log(json.data)
                if (json.data.state=='sold') thisOfClass.setState({selected_item_id:''})
                else thisOfClass.setState({history:json.data.hist})
            })
        }
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
    componentWillUnmount() {
        console.log('component will unmount')
        clearInterval(this.counter);
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
        for(var i=0; i<htmlCol.length-1;i++){
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
        var chart = {
            options: {
              chart: {
                id: "basic-bar"
              },
              xaxis: {
                categories: this.state.history.map((d)=> d.user.name_surname)
              }
            },
            series: [
              {
                name: "series-1",
                data: this.state.history.map((d)=> d.bid)
              }
            ]
          };
        console.log(chart.series, this.state.history)
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
                                            <div>{sell.current_price}₺</div>
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



<div className='bid_form' id="login-box">
  <div className="left">
    <h1>Make a Bid!</h1>
    <p>Title: { sell.item.title }</p>
    <p>Description: {sell.item.description}</p>
    <p>Type: {sell.item.item_type}</p>
    <p>Price: {chart.series[0].data[chart.series[0].data.length-1]}</p>
    <div id="form-send-bid">
        <input type={"text"} name={"amount"} placeholder={"0"}></input>
        <input type={"hidden"} name={"item_id"} value={sell.item.id}></input>
        <button className="submit-button" onClick={()=>this.clickHandler('bid')}>Bid!</button>
    </div>
  </div>
  
  <div className="right">
        <Chart
                options={chart.options}
                series={chart.series}
                type="bar"
                width="500"
                />
  </div>
  <div className="or">OR</div>
</div>
                </div>
            );
        }
    }

}
