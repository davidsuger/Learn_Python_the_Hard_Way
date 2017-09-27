from learn import parser
from nose.tools import assert_equal, assert_raises


def test_parse_verb():
    assert_equal(parser.parse_verb([('stop', 'is'), ('verb', 'run'), ('direction', 'north')]), ('verb', 'run'))
    assert_raises(parser.ParserError, parser.parse_verb, [('direction', 'north'), ('verb', 'run')])


def test_parse_object():
    assert_equal(parser.parse_object([('stop', 'is'), ('direction', 'north'), ('verb', 'run')]), ('direction', 'north'))
    assert_equal(parser.parse_object([('stop', 'is'), ('noun', 'bear'), ('verb', 'run')]), ('noun', 'bear'))
    assert_raises(parser.ParserError, parser.parse_object, [('verb', 'run'), ('direction', 'north')])


def test_parse_subject():
    assert_equal(parser.parse_subject([('stop', 'is'), ('verb', 'run'), ('direction', 'north')]), ('noun', 'player'))
    assert_equal(parser.parse_subject([('stop', 'is'), ('noun', 'bear'), ('verb', 'run')]), ('noun', 'bear'))
    assert_raises(parser.ParserError, parser.parse_subject, [('stop', 'of'), ('direction', 'north')])


def test_parse_sentence():
    s1 = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(s1.subject,'player')
    assert_equal(s1.verb,'run')
    assert_equal(s1.object,'north')
    s2 = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(s2.subject,'bear')
    assert_equal(s2.verb,'eat')
    assert_equal(s2.object,'honey')
    assert_raises(parser.ParserError, parser.parse_sentence, [('stop', 'of'), ('direction', 'north')])
