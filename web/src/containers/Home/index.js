// @flow
import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { css, StyleSheet } from 'aphrodite';
import { fetchChildren, createChild } from '../../actions/children';
import NewChildForm from '../../components/NewChildForm';
import Navbar from '../../components/Navbar';
import ChildListItem from '../../components/ChildListItem';

const styles = StyleSheet.create({
  card: {
    maxWidth: '500px',
    padding: '3rem 4rem',
    margin: '2rem auto',
  },
});

// type Child = {
//   id: number,
//   name: string,
// }

type Props = {
  children: Array<Children>,
  currentChildren: Array<Children>,
  fetchChildren: () => void,
  createChild: () => void
}

class Home extends Component {
  static contextTypes = {
    router: PropTypes.object,
  }

  componentDidMount() {
    this.props.fetchChildren(this.props.user);
  }

  props: Props

  handleNewChildSubmit = data => this.props.createChild(data, this.context.router);

  renderChildren() {
    const currentChildrenIds = [];
    this.props.currentChildren.map(child => currentChildrenIds.push(child.id));

    return this.props.children.map(child =>
      <ChildListItem
        key={child.id}
        room={child}
        currentChildrenIds={currentChildrenIds}
      />
    );
  }

  render() {
    return (
      <div style={{ flex: '1' }}>
        <Navbar />
        <div className={`card ${css(styles.card)}`}>
          <h3 style={{ marginBottom: '2rem', textAlign: 'center' }}>Add a child</h3>
          <NewChildForm onSubmit={this.handleNewChildSubmit} />
        </div>
        <div className={`card ${css(styles.card)}`}>
          <h3 style={{ marginBottom: '2rem', textAlign: 'center' }}>View someone's emotions</h3>
          {/* {this.renderChildren()} */}
        </div>
      </div>
    );
  }
}

export default connect(
  state => ({
    user: state.session.user,
    children: state.children.all,
    currentChildren: state.children.currentChildren,
  }),
  { fetchChildren, createChild }
)(Home);
