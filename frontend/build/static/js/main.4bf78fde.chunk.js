(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{20:function(e,t,n){},35:function(e,t,n){e.exports=n(66)},40:function(e,t,n){},41:function(e,t,n){},66:function(e,t,n){"use strict";n.r(t);var a=n(0),o=n.n(a),i=n(31),s=n.n(i),l=(n(40),n(2)),r=n(3),c=n(5),m=n(4),d=n(7),u=n(6),h=(n(41),n(20),n(21),n(32)),p=n.n(h),f=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={selected_item_id:"",sells:[{item:{id:"1",title:"Iphone X",owner:{name_surname:"Furkan Akyol"},item_type:"Phone",description:"\xc7iziksiz s\xfcper ikinci el telefon"},current_price:"10"},{item:{id:"2",title:"Mercedes C Coupe",owner:{name_surname:"Azad Baykara"},item_type:"Car",description:"100.000 kmde doktordan az kullan\u0131lm\u0131\u015f"},current_price:"300.000"}],history:[]},n.getData=n.getData.bind(Object(d.a)(n)),n}return Object(u.a)(t,e),Object(r.a)(t,[{key:"componentWillMount",value:function(){this.getData(),console.log("compenent will mount"),this.counter=setInterval(this.getData,1e3)}},{key:"getData",value:function(){var e=this;if(""==this.state.selected_item_id){var t=new XMLHttpRequest;t.addEventListener("load",(function(){0==JSON.parse(t.responseText).data.filter((function(t){return e.state.selected_item_id==t.id})).length?e.setState({selected_item_id:"",sells:JSON.parse(t.responseText).data}):e.setState({sells:JSON.parse(t.responseText).data})})),t.open("GET","http://localhost:8000/bid/test/"),t.send()}else{var n=new Request("http://localhost:8000/bid/asd/"+this.state.selected_item_id,{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),a={csrfmiddlewaretoken:this.getCookie("csrftoken")},o=this;fetch(n,{method:"POST",mode:"same-origin",body:JSON.stringify(a)}).then((function(e){return e.json()})).then((function(e){console.log(e.data),"sold"==e.data.state?o.setState({selected_item_id:""}):o.setState({history:e.data.hist})}))}}},{key:"watchItem",value:function(e){var t=new Request("http://localhost:8000/bid/watch-sell/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),n={csrfmiddlewaretoken:this.getCookie("csrftoken"),item_id:e};fetch(t,{method:"POST",mode:"same-origin",body:JSON.stringify(n)}).then((function(e){return e.json()})).then((function(e){console.log(e)}))}},{key:"componentWillUnmount",value:function(){console.log("component will unmount"),clearInterval(this.counter)}},{key:"sendBidReq",value:function(){for(var e=new Request("http://localhost:8000/bid/bidding/1",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=document.getElementById("form-send-bid").children,a=0;a<n.length-1;a++)t[n[a].name]=n[a].value;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log(e)}))}},{key:"clickHandler",value:function(e){console.log(e),"bid"===e?this.sendBidReq():"fa fa-bell"===e.target.className?this.watchItem(e.currentTarget.id):this.setState({selected_item_id:e.currentTarget.id})}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var o=n[a].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}},{key:"render",value:function(){var e=this,t={options:{chart:{id:"basic-bar"},xaxis:{categories:this.state.history.map((function(e){return e.user.name_surname}))}},series:[{name:"series-1",data:this.state.history.map((function(e){return e.bid}))}]};if(console.log(t.series,this.state.history),""==this.state.selected_item_id)return o.a.createElement("div",null,o.a.createElement("h1",null,"Current Auctions:"),this.state.sells.map((function(t){return o.a.createElement("div",{onClick:function(t){return e.clickHandler(t)},id:t.id,className:"card"},o.a.createElement("div",{className:"additional"},o.a.createElement("div",{className:"item-image"},o.a.createElement("i",{className:"fa fa-bell"}),o.a.createElement("img",{src:"https://www.dhresource.com/600x600/f2/albu/g7/M01/D3/91/rBVaSVrsd5aAA5isAAMVt25ugBc771.jpg",alt:"Item Photo"}),o.a.createElement("div",{className:"item-price"},o.a.createElement("div",null,t.current_price,"\u20ba")))),o.a.createElement("div",{className:"general"},o.a.createElement("div",{className:"item-info"},o.a.createElement("p",{className:"left"}," Owner: ",t.item.owner.name_surname),o.a.createElement("p",{className:"right"},"Type: ",t.item.item_type)),o.a.createElement("h1",null,t.item.title),o.a.createElement("p",null,t.item.description),o.a.createElement("span",null,"Click On Item to Go Auction Page")))})));var n=this.state.sells.filter((function(t){return t.id==e.state.selected_item_id}))[0];this.getCookie("csrftoken");return o.a.createElement("div",null,o.a.createElement("button",{onClick:function(){return e.setState({selected_item_id:""})}},"all items"),o.a.createElement("div",{className:"bid_form",id:"login-box"},o.a.createElement("div",{className:"left"},o.a.createElement("h1",null,"Make a Bid!"),o.a.createElement("p",null,"Title: ",n.item.title),o.a.createElement("p",null,"Description: ",n.item.description),o.a.createElement("p",null,"Type: ",n.item.item_type),o.a.createElement("p",null,"Price: ",t.series[0].data[t.series[0].data.length-1]),o.a.createElement("div",{id:"form-send-bid"},o.a.createElement("input",{type:"text",name:"amount",placeholder:"0"}),o.a.createElement("input",{type:"hidden",name:"item_id",value:n.item.id}),o.a.createElement("button",{className:"submit-button",onClick:function(){return e.clickHandler("bid")}},"Bid!"))),o.a.createElement("div",{className:"right"},o.a.createElement(p.a,{options:t.options,series:t.series,type:"bar",width:"500"})),o.a.createElement("div",{className:"or"},"OR")))}}]),t}(o.a.Component),g=function(e){function t(e){return Object(l.a)(this,t),Object(c.a)(this,Object(m.a)(t).call(this,e))}return Object(u.a)(t,e),Object(r.a)(t,[{key:"componentWillMount",value:function(){var e=new XMLHttpRequest;e.addEventListener("load",(function(){})),e.open("GET","http://localhost:8000/home/deneme"),e.send()}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var o=n[a].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}},{key:"render",value:function(){return o.a.createElement("div",null,o.a.createElement("form",{action:"http://localhost:8000/login/",method:"POST"},o.a.createElement("input",{type:"hidden",name:"csrfmiddlewaretoken",value:this.getCookie("csrftoken")}),o.a.createElement("fieldset",{className:"form-group"},o.a.createElement("legend",{className:"border-bottom mb-4"},"Log In"),o.a.createElement("label",{for:"id_username"},"Username:"),o.a.createElement("input",{type:"text",name:"username",autofocus:"",autocapitalize:"none",autocomplete:"username",maxlength:"150",required:"",id:"id_username"}),o.a.createElement("label",{for:"id_password"},"Password:"),o.a.createElement("input",{type:"password",name:"password",autocomplete:"current-password",required:"",id:"id_password"})),o.a.createElement("div",{className:"form-group"},o.a.createElement("input",{type:"submit",value:"Log In!"}))))}}]),t}(o.a.Component),k=n(13),b=n(12),y=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).clickHandler=n.clickHandler.bind(Object(d.a)(n)),n}return Object(u.a)(t,e),Object(r.a)(t,[{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var o=n[a].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}},{key:"clickHandler",value:function(){var e=new Request("http://localhost:8000/home/add_item/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={title:this.title.value,description:this.description.value,item_type:this.item_type.value,csrfmiddlewaretoken:this.getCookie("csrftoken")};fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){console.log(e)}))}},{key:"render",value:function(){var e=this;return o.a.createElement("div",{className:"bid_form",id:"login-box"},o.a.createElement("div",{className:"center"},o.a.createElement("h1",null,"Add Item"),o.a.createElement("input",{type:"text",ref:function(t){return e.title=t},name:"title",placeholder:"Title"}),o.a.createElement("input",{type:"text",ref:function(t){return e.description=t},name:"description",placeholder:"Description"}),o.a.createElement("input",{type:"text",ref:function(t){return e.item_type=t},name:"item_type",placeholder:"Item type"}),o.a.createElement("button",{className:"submit-button",onClick:this.clickHandler},"Submit")))}}]),t}(o.a.Component),v=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={},n.addBalance=n.addBalance.bind(Object(d.a)(n)),n.changePassword=n.changePassword.bind(Object(d.a)(n)),n.watchItemType=n.watchItemType.bind(Object(d.a)(n)),n}return Object(u.a)(t,e),Object(r.a)(t,[{key:"componentWillMount",value:function(){var e=new Request("http://localhost:8000/profile/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log(e),n.setState({name_surname:e.data.name_surname,email:e.data.email,balance:e.data.balance})}));e=new Request("http://localhost:8000/bid/user-history/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log("!!!!!!!!!!! history",e),n.setState({hist:e.data})}))}},{key:"addBalance",value:function(){var e=new Request("http://localhost:8000/home/add_balance/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={amount:document.getElementById("amount-value").value,csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){"Success"==e.result&&n.setState({name_surname:e.data.name_surname,email:e.data.email,balance:e.data.balance})}))}},{key:"watchItemType",value:function(){var e=new Request("http://localhost:8000/bid/watch-item-type/"+document.getElementById("item-type-watch").value);fetch(e,{method:"GET"}).then((function(e){return e.json()}))}},{key:"changePassword",value:function(){var e=new Request("http://localhost:8000/home/change_password/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={old_password:document.getElementById("old-password").value,new_password:document.getElementById("new-password").value,csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){"Success"==e.result?(console.log("SUCCESS"),n.setState({change_password_message:"Password is changed successfully"})):(console.log("FAIL"),n.setState({change_password_message:"Password is incorrect"}))}))}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var o=n[a].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}},{key:"render",value:function(){return o.a.createElement("div",null,o.a.createElement("p",null," Ad Soyad: ",this.state.name_surname),o.a.createElement("p",null," Email: ",this.state.email),o.a.createElement("p",null," Bakiye: ",this.state.balance),o.a.createElement("hr",null),o.a.createElement("input",{class:"form-control",type:"text",id:"amount-value",name:"amount",placeholder:"0"}),o.a.createElement("button",{onClick:this.addBalance},"Add Balance"),o.a.createElement("hr",null),o.a.createElement("input",{type:"password",class:"form-control",id:"old-password",placeholder:"Old Password"}),o.a.createElement("input",{type:"password",class:"form-control",id:"new-password",placeholder:"New Password"}),o.a.createElement("button",{onClick:this.changePassword},"Change Password"),this.state.change_password_message?o.a.createElement("p",null,this.state.change_password_message):null,o.a.createElement("hr",null),o.a.createElement("input",{type:"text",class:"form-control",name:"item_type",placeholder:"item type to watch",id:"item-type-watch"}),o.a.createElement("button",{onClick:this.watchItemType},"Submit"),o.a.createElement("p",null,"sold:"),this.state.hist?this.state.hist.owned_sells.map((function(e){return o.a.createElement("div",{style:{background:"red",margin:"20px",padding:"10px;"}},o.a.createElement("p",null,"item: ",e.item.title),o.a.createElement("p",null,"sold price: ",e.current_price))})):"",o.a.createElement("p",null,"won:"),this.state.hist?this.state.hist.won_sellls.map((function(e){return o.a.createElement("div",{style:{background:"red",margin:"20px",padding:"10px;"}},o.a.createElement("p",null,"item: ",e.item.title),o.a.createElement("p",null,"paid price: ",e.current_price))})):"")}}]),t}(o.a.Component),E=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={selected_item_id:"",items:[]},n.toggleDisplay=n.toggleDisplay.bind(Object(d.a)(n)),n}return Object(u.a)(t,e),Object(r.a)(t,[{key:"componentWillMount",value:function(){var e=new Request("http://localhost:8000/bid/list-items/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log(e),n.setState({items:e.data})}))}},{key:"clickHandler",value:function(e){console.log(e.currentTarget.id),this.setState({selected_item_id:e.currentTarget.id})}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var o=n[a].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}},{key:"toggleDisplay",value:function(e,t){console.log(t);var n=e.getElementsByClassName(t)[0].style.display;e.getElementsByClassName("instant-increment-form")[0].style.display="none",e.getElementsByClassName("increment-form")[0].style.display="none",e.getElementsByClassName("decrement-form")[0].style.display="none",e.getElementsByClassName(t)[0].style.display="none"==n?"block":"none",e.style.height="none"==n?"decrement-form"==t?"500px":"350px":"200px"}},{key:"clickHandler",value:function(e){console.log(e.target.parentNode.children),this.sendPost(e.target.parentNode)}},{key:"sendPost",value:function(e){for(var t=new Request("http://localhost:8000/bid/sell/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),n={csrfmiddlewaretoken:this.getCookie("csrftoken")},a=e.children,o=0;o<a.length-1;o++)n[a[o].name]=a[o].value;fetch(t,{method:"POST",mode:"same-origin",body:JSON.stringify(n)}).then((function(e){return e.json()})).then((function(e){console.log(e)}))}},{key:"render",value:function(){var e=this;return o.a.createElement("div",null,o.a.createElement("h1",null,"Owned Items"),o.a.createElement("div",{className:"list-wrapper"},this.state.items.map((function(t){return o.a.createElement("div",{id:t.id,className:"card"},o.a.createElement("div",{className:"additional"},o.a.createElement("div",{className:"item-image"},o.a.createElement("img",{src:"https://www.dhresource.com/600x600/f2/albu/g7/M01/D3/91/rBVaSVrsd5aAA5isAAMVt25ugBc771.jpg",alt:"Item Photo"}))),o.a.createElement("div",{className:"general"},o.a.createElement("div",{className:"item-info"},o.a.createElement("p",{className:"left"}," Owner: ",t.owner.name_surname),o.a.createElement("p",{className:"right"},"Type: ",t.item_type)),o.a.createElement("h1",null,t.title),o.a.createElement("p",null,t.description),o.a.createElement("div",null,o.a.createElement("div",{className:"btn-group"},o.a.createElement("button",{className:"btn btn-success btn-sm",onClick:function(){return e.toggleDisplay(document.getElementById(t.id),"decrement-form")}},"Decrement"),o.a.createElement("button",{className:"btn btn-success btn-sm",onClick:function(){return e.toggleDisplay(document.getElementById(t.id),"increment-form")}},"Increment"),o.a.createElement("button",{className:"btn btn-success btn-sm",onClick:function(){return e.toggleDisplay(document.getElementById(t.id),"instant-increment-form")}},"Instant")),o.a.createElement("div",{className:"form decrement-form",style:{display:"none"}},o.a.createElement("fieldset",{className:"form-group"},o.a.createElement("input",{type:"text",name:"starting_price",placeholder:"starting price"}),o.a.createElement("input",{type:"text",name:"period",placeholder:"period"}),o.a.createElement("input",{type:"text",name:"delta",placeholder:"delta"}),o.a.createElement("input",{type:"text",name:"stop_decrement",placeholder:"stop decrement"}),o.a.createElement("input",{type:"hidden",name:"item_id",defaultValue:t.id}),o.a.createElement("input",{type:"hidden",name:"sell_type",defaultValue:"decrement"}),o.a.createElement("button",{style:{borderRadius:0},className:"btn btn-success btn-sm",onClick:function(t){return e.clickHandler(t)}},"Decrement"))),o.a.createElement("div",{className:"form increment-form",style:{display:"none"}},o.a.createElement("fieldset",{className:"form-group"},o.a.createElement("input",{type:"text",name:"starting_price",placeholder:"starting price"}),o.a.createElement("input",{type:"text",name:"instant_sell",placeholder:"instant sell"}),o.a.createElement("input",{type:"hidden",name:"item_id",defaultValue:t.id}),o.a.createElement("input",{type:"hidden",name:"sell_type",defaultValue:"increment"}),o.a.createElement("button",{style:{borderRadius:0},className:"btn btn-success btn-sm",onClick:function(t){return e.clickHandler(t)}},"Increment"))),o.a.createElement("div",{className:"form instant-increment-form",style:{display:"none"}},o.a.createElement("fieldset",{className:"form-group"},o.a.createElement("input",{type:"text",name:"starting_price",placeholder:"starting price"}),o.a.createElement("input",{type:"text",name:"instant_sell",placeholder:"instant sell"}),o.a.createElement("input",{type:"hidden",name:"item_id",defaultValue:t.id}),o.a.createElement("input",{type:"hidden",name:"sell_type",defaultValue:"instant-increment"}),o.a.createElement("button",{style:{borderRadius:0},className:"btn btn-success btn-sm",onClick:function(t){return e.clickHandler(t)}},"Instant"))))))}))))}}]),t}(o.a.Component),w=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={messages:[]},n}return Object(u.a)(t,e),Object(r.a)(t,[{key:"componentWillMount",value:function(){var e=new Request("http://localhost:8000/bid/messages/",{headers:{"X-CSRFToken":this.getCookie("csrftoken")}}),t={csrfmiddlewaretoken:this.getCookie("csrftoken")},n=this;fetch(e,{method:"POST",mode:"same-origin",body:JSON.stringify(t)}).then((function(e){return e.json()})).then((function(e){console.log(e),n.setState({messages:e.data})}))}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var o=n[a].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}},{key:"render",value:function(){return o.a.createElement("div",null,this.state.messages.map((function(e){return o.a.createElement("p",null,e)})))}}]),t}(o.a.Component),C=(n(62),function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(c.a)(this,Object(m.a)(t).call(this,e))).state={route:"",message_count:-1,isMessage:0},n.getCookie=n.getCookie.bind(Object(d.a)(n)),n}return Object(u.a)(t,e),Object(r.a)(t,[{key:"clickHandler",value:function(e){console.log(document.getElementsByClassName("nav-button"));for(var t=document.getElementsByClassName("nav-button"),n=0;n<t.length;n++)t[n].id===e.target.id?t[n].className=t[n].className+" active":t[n].className=t[n].className.split(" ")[0]}},{key:"socketConnection",value:function(){var e=new WebSocket("ws://localhost:8000/ws/time/");e.onmessage=function(e){var t=JSON.parse(e.data);console.log(t)},e.onclose=function(e){console.error("Chat socket closed unexpectedly")}}},{key:"componentWillMount",value:function(){var e=this;this.socketConnection();setInterval((function(){return e.getMessages(e)}),1e3);console.log("daskhdkjasdjkashdkjashdkjashk")}},{key:"getCookie",value:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var o=n[a].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}},{key:"getMessages",value:function(e){var t=new Request("http://localhost:8000/bid/messages/",{headers:{"X-CSRFToken":e.getCookie("csrftoken")}}),n={csrfmiddlewaretoken:e.getCookie("csrftoken")},a=e;fetch(t,{method:"POST",mode:"same-origin",body:JSON.stringify(n)}).then((function(e){return e.json()})).then((function(t){if(console.log(t),"Fail"!=t.result){if(-1!=e.state.message_count&&e.state.message_count<t.data.length)return void a.setState({message_count:t.data.length,isMessage:1});a.setState({message_count:t.data.length})}}))}},{key:"render",value:function(){var e=this;return o.a.createElement("div",null,o.a.createElement("link",{href:"https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",rel:"stylesheet"}),o.a.createElement("div",{class:"topnav"}),o.a.createElement(k.a,null,o.a.createElement("div",{class:"topnav"},o.a.createElement(k.b,{className:"nav-button",id:"home-button",onClick:function(t){return e.clickHandler(t)},to:"/bid"},"Home"),o.a.createElement(k.b,{className:"nav-button",id:"add-button",onClick:function(t){return e.clickHandler(t)},to:"/add-item"},"Add Item"),o.a.createElement(k.b,{className:"nav-button",id:"profile-button",onClick:function(t){return e.clickHandler(t)},to:"/profile"},"My Profile"),o.a.createElement(k.b,{className:"nav-button",id:"list-button",onClick:function(t){return e.clickHandler(t)},to:"/list-items"},"List My Items"),o.a.createElement(k.b,{className:"nav-button",id:"message-button",onClick:function(t){e.setState({isMessage:0}),e.clickHandler(t)},to:"/messages"},o.a.createElement("i",{style:{fontSize:"20px",color:this.state.isMessage?"red":"gold"},className:"fa fa-bell"})),o.a.createElement("a",{className:"nav-button",id:"logout-button",href:"/logout",style:{float:"right"}},"Logout"),o.a.createElement(k.b,{className:"nav-button",id:"admin-button",onClick:function(t){return e.clickHandler(t)},style:{float:"right"},to:"/profile"},"Admin")),o.a.createElement(b.a,{path:"/bid",component:f}),o.a.createElement(b.a,{path:"/login",component:g}),o.a.createElement(b.a,{path:"/add-item",component:y}),o.a.createElement(b.a,{path:"/profile",component:v}),o.a.createElement(b.a,{path:"/list-items",component:E}),o.a.createElement(b.a,{path:"/messages",component:w})))}}]),t}(o.a.Component));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));s.a.render(o.a.createElement(C,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[35,1,2]]]);
//# sourceMappingURL=main.4bf78fde.chunk.js.map