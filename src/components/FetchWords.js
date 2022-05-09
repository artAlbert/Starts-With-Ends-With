import React from 'react';

export default class FetchWords extends React.Component {
    state = {
        loading: true,
        words: [],
        wordCount: ""
    };

    async componentDidMount() {
        const url = '/starts-with-ends-with?first=t&last=y';
        const response = await fetch(url);
        const data = await response.json();
        this.setState({ loading: false, words: data.words, wordCount: data.count });
    }

    render() {
        return (
            <div>
                {this.state.loading 
                    ? <div> Loading data... </div>
                    : <div>
                        Matches: {this.state.wordCount}
                        {this.state.words.map(wordPair => (
                            <div>
                                <div> {wordPair.word} : {wordPair.meaning} </div>
                            </div>
                        ))}
                    </div>
                }
            </div>
        )
    }
}     