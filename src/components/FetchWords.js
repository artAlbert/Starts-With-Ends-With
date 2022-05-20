import React from 'react';

export default class FetchWords extends React.Component {

    state = {
        noInput: true,
        words: [],
        wordCount: "",
    };
        
    async componentDidMount() {
        //Initialize variables
        var firstInput = this.props.firstLetter;
        var lastInput = this.props.lastLetter;
        var url = "";

        //startsWith AND endsWith
        if (this.props.firstEqualsLast) {
            //valid input
            if (firstInput.trim() != "") {
                //POST request to API and 
                url = `https://flask-service.6bfcrl4vtikjs.us-east-2.cs.amazonlightsail.com/starts-and-ends-with?letter=${firstInput}`
                const response = await fetch(url);
                const data = await response.json();
                this.setState({ noInput: false, words: data.words, wordCount: data.count});
            }
        }
        //startsWith - endsWith
        else {
            //valid input
            if (firstInput.trim() != "" && lastInput.trim() != "") {
                url = `https://flask-service.6bfcrl4vtikjs.us-east-2.cs.amazonlightsail.com/starts-with-ends-with?first=${firstInput}&last=${lastInput}`
                const response = await fetch(url);
                const data = await response.json();
                this.setState({ noInput: false, words: data.words, wordCount: data.count});
            }
        }
    } 

    render() {
        return (
            <div>
                {this.state.noInput 
                    ? [this.props.firstEqualsLast ? <div key="1"> Enter a letter </div> : <div key="2"> Enter a first and last letter </div>]
                    : <div>
                        Matches: {this.state.wordCount}
                        {this.state.words.map(wordPair => (
                            <div key={wordPair.word_id}>
                                <div> {wordPair.word} : {wordPair.meaning} </div>
                                <br></br>
                            </div>
                        ))}
                    </div>
                }
            </div>
        )
    }
}     