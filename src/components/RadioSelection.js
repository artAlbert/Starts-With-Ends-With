import React from 'react';
import PostForm from './PostForm';

export default class RadioSelection extends React.Component {
    
    state = {
        firstEqualsLast: "",
    };

    handleChange = (event) => {
        event.target.value === "same"
        ? this.setState({firstEqualsLast: true})
        : this.setState({firstEqualsLast: false});
    }

    render() {
        return (
          <div>
            <h1>Starts With Ends With...</h1>
            <input type="radio" value="same" name="selector" onChange={this.handleChange.bind(this)}/> the same letter 
            <br></br>
            <input type="radio" value="different" name="selector" onChange={this.handleChange.bind(this)}/> different letters
            <PostForm key={this.state.firstEqualsLast} firstEqualsLast={this.state.firstEqualsLast}/>
          </div>
        );
    }
}