(this.webpackJsonptab_bar=this.webpackJsonptab_bar||[]).push([[0],{16:function(e,t,a){e.exports=a(24)},24:function(e,t,a){"use strict";a.r(t);var n=a(6),r=a.n(n),c=a(13),l=a.n(c),s=a(0),o=a(3),i=a(1),u=a(2),d=a(14),m=a.n(d),f=a(11),p=function(e){Object(i.a)(a,e);var t=Object(u.a)(a);function a(e){var n;return Object(s.a)(this,a),(n=t.call(this,e)).state={numClicks:0,selectedId:1,list:[]},n.MenuItem=function(e){var t=e.item,a=e.selectedId;return r.a.createElement("div",{className:"menu-item ".concat(a==t.id?"active":"")},r.a.createElement("div",null,t.title),r.a.createElement("div",{style:{fontWeight:"normal",fontStyle:"italic"}},t.description))},n.Arrow=function(e){var t=e.text,a=e.className;return r.a.createElement("div",{className:a},t)},n.ArrowLeft=n.Arrow({text:"<",className:"arrow-prev"}),n.ArrowRight=n.Arrow({text:">",className:"arrow-next"}),n.render=function(){return r.a.createElement("div",null,r.a.createElement(m.a,{alignCenter:!1,data:n.Menu(n.state.list,n.state.selectedId),wheel:!0,scrollToSelected:!0,selected:"".concat(n.state.selectedId),onSelect:n.onSelect}),r.a.createElement("hr",{style:{borderColor:"var(--primary-color)"}}))},n.onSelect=function(e){n.setState((function(t,a){return{selectedId:e}}),(function(){return f.a.setComponentValue(e)}))},n.state.list=n.props.args.data,n.state.selectedId=n.props.args.selectedId,n}return Object(o.a)(a,[{key:"Menu",value:function(e,t){var a=this;return e.map((function(e){return r.a.createElement(a.MenuItem,{item:e,selectedId:t,key:e.id})}))}}]),a}(f.b),v=Object(f.c)(p);l.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(v,null)),document.getElementById("root"))}},[[16,1,2]]]);
//# sourceMappingURL=main.f2101ed2.chunk.js.map