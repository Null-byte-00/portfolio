import "@picocss/pico"
import React from "react"

class Navbar extends React.Component {
    render() {
        return (
            <article>
            <nav>
                <ul>
                    <li><strong>Acme Corp</strong></li>
                    </ul>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Projects</a></li>
                        <li><a href="#">Articles</a></li>
                        <li><a href="#">Experience</a></li>
                        <li><a href="#">Resume</a></li>
                        <li><a href="#">About</a></li>
                </ul>
            </nav>
            </article>
        )
    }
}

export default Navbar