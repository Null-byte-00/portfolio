import React, { Component } from "react";
import { render } from "react-dom";
import Navbar from "./components/navbar"
import Resume from "./components/details"
import Articles from "./components/articles"
import Projects from "./components/projects"

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Navbar/>
        <h1>This is my website</h1>
        {this.GetCurrentPage()}
      </div>
    );
  }

  GetCurrentPage () {
    var hash = document.location.hash.substring(1);
    if (hash == "Projects") {
      return (
        <Projects />
      )
    } else if (hash == "Articles") {
      return (
        <Articles />
      )
    } else if (hash == "Resume") {
      return (
        <Resume />
      )
    } else {
      return (
        <h1>Home</h1>
      )
    }
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);