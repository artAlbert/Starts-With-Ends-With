import React from 'react';
import FetchWords from './FetchWords';

export default class PostForm extends React.Component {

    state = {

        userInput: "",
        firstLetter: "",
        lastLetter: "",
        firstEqualsLast: this.props.firstEqualsLast,

    };

    handleChangeFirst = (event) => {
        this.setState({userInput: event.target.value});
    }

    handleChangeLast = (event) => {
        this.setState({lastLetter: event.target.value});
    }

    handleSubmit() {
        this.state.firstEqualsLast
        ? this.setState({firstLetter: this.state.userInput})
        : this.setState({firstLetter: this.state.userInput, lastLetter: this.state.lastLetter})
    }

    render() {
        return (
            <div>
                {this.state.firstEqualsLast
                    ?   <div>
                            <input value={this.state.userInput} onChange={this.handleChangeFirst.bind(this)} onSubmit={this.handleSubmit.bind(this)} maxLength='1' />
                            <button onClick={this.handleSubmit.bind(this)}> Submit </button>
                            <FetchWords key={this.state.firstLetter} firstLetter={this.state.firstLetter} firstEqualsLast={this.state.firstEqualsLast} />
                        </div>
                    :   <div>
                            <input value={this.state.userInput} onChange={this.handleChangeFirst.bind(this)} onSubmit={this.handleSubmit.bind(this)} maxLength='1' />
                            <input value={this.state.lastLetter} onChange={this.handleChangeLast.bind(this)} onSubmit={this.handleSubmit.bind(this)}maxLength='1'/>
                            <button onClick={this.handleSubmit.bind(this)}> Submit </button>
                            <FetchWords key={`${this.state.firstLetter}${this.state.lastLetter}`} firstLetter={this.state.firstLetter} lastLetter={this.state.lastLetter} firstEqualsLast={this.state.firstEqualsLast} />
                        </div> 
                }
            </div>
        );
    }
}