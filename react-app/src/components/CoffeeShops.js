import React, { Component } from 'react';

class CoffeeShops extends Component {

constructor () {
  super();
  this.state = {
    coffeeshops: []
  };
};

componentDidMount() {
  fetch('/api/v1.0/coffeeshops').then(results =>{
    console.log(results)
    return results.json();
  }).then(data=>{
    console.log(data)
    console.log(data.coffeeshops)
    let shops = data.coffeeshops.map((shop) =>{
      return(
        //TODO need to chage these references "shop.name" and other to json to the correct ones once using real db
        <div key={shop.name} className="col">
          <li>
            <a href="/shops/coffeeidFIXTHIS">
              <img src={shop.photo} style={{width: 300, height: 300}} alt="Photo1" />
              <span className="picText"><span> name <br /><br />location<br />Price:<br />Rating:</span></span>
            </a>
          </li>
        </div>
      )
    })
    this.setState({coffeeshops: shops});
    console.log("state", this.state.coffeeshops);
  })
}

render() {
    console.log(this.state.coffeeshops);

    return (
      <div className = "CoffeeShops">
        {/*location dropdown*/}
        <div className="container">
          <div className="dropdown">
            <button id="city-btn" className="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown" onclick="myFunction()">Choose City
              <span className="caret" /></button>
            <ul className="dropdown-menu">
              <input className="form-control" id="myInput" type="text" placeholder="Search.." />
              <li><a href="#">Austin, TX</a></li>
            </ul>
          </div>
        </div>
        <section className="page-section">
          <div className="container">
            <div className="row">
              <ul className="img-list">
                {this.state.coffeeshops}
              </ul>
            </div>
          </div>
        </section>
      </div>
    );
  }
}

export default CoffeeShops;