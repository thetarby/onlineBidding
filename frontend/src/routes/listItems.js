import React from 'react';
import './bid.css';
import axios from 'axios'
export default class ListItems extends React.Component {
    constructor(props){
        super(props)
        this.state={
            selected_item_id:'',
            items:[]
        }
        this.toggleDisplay=this.toggleDisplay.bind(this)
    }

    componentWillMount(){
        var request = new Request(
            'http://localhost:8000/bid/list-items/',
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
            thisOfClass.setState(
                {
                    items:json.data
            })
        })

    }

    clickHandler(e){
        console.log(e.currentTarget.id)
        this.setState({selected_item_id:e.currentTarget.id})
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
    toggleDisplay(el,className) {
        console.log(className)
        var old=el.getElementsByClassName(className)[0].style.display
        el.getElementsByClassName('instant-increment-form')[0].style.display='none'
        el.getElementsByClassName('increment-form')[0].style.display='none'
        el.getElementsByClassName('decrement-form')[0].style.display='none'
        el.getElementsByClassName(className)[0].style.display = old=='none' ? 'block' : 'none'
        el.style.height = old=='none' ? ( className=='decrement-form' ? '500px' : '350px') : '200px'
    }
    clickHandler(e){
        console.log(e.target.parentNode.children)
        this.sendPost(e.target.parentNode)
    }
    sendPost(el){
        var request = new Request(
            'http://localhost:8000/bid/sell/',
            {headers: {'X-CSRFToken': this.getCookie('csrftoken')}}
        );
        var data = {
            csrfmiddlewaretoken:this.getCookie('csrftoken')
        };
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
    render(){
        return(
            <div>
                <h1>Owned Items</h1>
                <div className="list-wrapper">
                {
                    this.state.items.map((item)=>
                        <div id={item.id} className="card">
                            <div className="additional">
                            <div className="item-image">
                                <img src="https://www.dhresource.com/600x600/f2/albu/g7/M01/D3/91/rBVaSVrsd5aAA5isAAMVt25ugBc771.jpg" alt="Item Photo" />

                            </div>
                            </div>
                            <div className="general">
                            <div className="item-info">
                                <p className="left"> Owner: { (item.owner.name_surname) }</p>
                                <p className="right">Type: {item.item_type }</p>
                            </div>
                            <h1>{item.title}</h1>
                            <p>{item.description}</p>
                            <div>
                            <div className="btn-group">
                                <button className={"btn btn-success btn-sm"} onClick={()=>this.toggleDisplay(document.getElementById(item.id) ,'decrement-form')}>Decrement</button>
                                <button className={"btn btn-success btn-sm"} onClick={()=>this.toggleDisplay(document.getElementById(item.id) ,'increment-form')}>Increment</button>
                                <button className={"btn btn-success btn-sm"} onClick={()=>this.toggleDisplay(document.getElementById(item.id) ,'instant-increment-form')}>Instant</button>
                            </div>
                            <div className="form decrement-form" style={{display: 'none'}}>
                                <fieldset className="form-group">
                                <input type="text" name="starting_price" placeholder="starting price" />
                                <input type="text" name="period" placeholder="period" />
                                <input type="text" name="delta" placeholder="delta" />
                                <input type="text" name="stop_decrement" placeholder="stop decrement" />
                                <input type="hidden" name="item_id" defaultValue={item.id} />
                                <input type="hidden" name="sell_type" defaultValue="decrement" />
                                <button style={{borderRadius:0}} className="btn btn-success btn-sm" onClick={(e)=>this.clickHandler(e)}>Decrement</button>

                                </fieldset>
                            </div>
                            <div className="form increment-form" style={{display: 'none'}}>
                                <fieldset className="form-group">
                                <input type="text" name="starting_price" placeholder="starting price" />
                                <input type="text" name="instant_sell" placeholder="instant sell" />
                                <input type="hidden" name="item_id" defaultValue={item.id} />
                                <input type="hidden" name="sell_type" defaultValue="increment" />
                                <button style={{borderRadius:0}} className="btn btn-success btn-sm" onClick={(e)=>this.clickHandler(e)}>Increment</button>

                                </fieldset>
                            </div>
                            <div className="form instant-increment-form" style={{display: 'none'}}>
                                <fieldset className="form-group">
                                <input type="text" name="starting_price" placeholder="starting price" />
                                <input type="text" name="instant_sell" placeholder="instant sell" />
                                <input type="hidden" name="item_id" defaultValue={item.id} />
                                <input type="hidden" name="sell_type" defaultValue="instant-increment" />
                                <button style={{borderRadius:0}} className="btn btn-success btn-sm" onClick={(e)=>this.clickHandler(e)}>Instant</button>

                                </fieldset>
                            </div>
                            </div>
                            </div>
                        </div>
                    )
                    
                }
                </div>
            </div>

        );
    }

}
