"""
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// @generated by gentest/gentest.rb from gentest/fixtures/YGFlexDirectionTest.html
"""
import pytest
import yoga


def test_flex_direction_column_no_height():
    config = yoga.Config()

    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_ABSOLUTE_PERCENTAGE_AGAINST_PADDING_EDGE, True)
    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_FIX_ABSOLUTE_TRAILING_COLUMN_MARGIN, True)

    root = yoga.Node(config)
    root.set_width(100)

    root_child0 = yoga.Node(config)
    root_child0.set_height(10)
    root.insert_child(root_child0, 0)

    root_child1 = yoga.Node(config)
    root_child1.set_height(10)
    root.insert_child(root_child1, 1)

    root_child2 = yoga.Node(config)
    root_child2.set_height(10)
    root.insert_child(root_child2, 2)
    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_LTR);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 30

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 100
    assert root_child0.get_computed_height() == 10

    assert root_child1.get_computed_left() == 0
    assert root_child1.get_computed_top() == 10
    assert root_child1.get_computed_width() == 100
    assert root_child1.get_computed_height() == 10

    assert root_child2.get_computed_left() == 0
    assert root_child2.get_computed_top() == 20
    assert root_child2.get_computed_width() == 100
    assert root_child2.get_computed_height() == 10

    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_RTL);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 30

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 100
    assert root_child0.get_computed_height() == 10

    assert root_child1.get_computed_left() == 0
    assert root_child1.get_computed_top() == 10
    assert root_child1.get_computed_width() == 100
    assert root_child1.get_computed_height() == 10

    assert root_child2.get_computed_left() == 0
    assert root_child2.get_computed_top() == 20
    assert root_child2.get_computed_width() == 100
    assert root_child2.get_computed_height() == 10


def test_flex_direction_row_no_width():
    config = yoga.Config()

    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_ABSOLUTE_PERCENTAGE_AGAINST_PADDING_EDGE, True)
    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_FIX_ABSOLUTE_TRAILING_COLUMN_MARGIN, True)

    root = yoga.Node(config)
    root.set_flex_direction(yoga.FLEX_DIRECTION_ROW)
    root.set_height(100)

    root_child0 = yoga.Node(config)
    root_child0.set_width(10)
    root.insert_child(root_child0, 0)

    root_child1 = yoga.Node(config)
    root_child1.set_width(10)
    root.insert_child(root_child1, 1)

    root_child2 = yoga.Node(config)
    root_child2.set_width(10)
    root.insert_child(root_child2, 2)
    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_LTR);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 30
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 10
    assert root_child0.get_computed_height() == 100

    assert root_child1.get_computed_left() == 10
    assert root_child1.get_computed_top() == 0
    assert root_child1.get_computed_width() == 10
    assert root_child1.get_computed_height() == 100

    assert root_child2.get_computed_left() == 20
    assert root_child2.get_computed_top() == 0
    assert root_child2.get_computed_width() == 10
    assert root_child2.get_computed_height() == 100

    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_RTL);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 30
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 20
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 10
    assert root_child0.get_computed_height() == 100

    assert root_child1.get_computed_left() == 10
    assert root_child1.get_computed_top() == 0
    assert root_child1.get_computed_width() == 10
    assert root_child1.get_computed_height() == 100

    assert root_child2.get_computed_left() == 0
    assert root_child2.get_computed_top() == 0
    assert root_child2.get_computed_width() == 10
    assert root_child2.get_computed_height() == 100


def test_flex_direction_column():
    config = yoga.Config()

    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_ABSOLUTE_PERCENTAGE_AGAINST_PADDING_EDGE, True)
    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_FIX_ABSOLUTE_TRAILING_COLUMN_MARGIN, True)

    root = yoga.Node(config)
    root.set_width(100)
    root.set_height(100)

    root_child0 = yoga.Node(config)
    root_child0.set_height(10)
    root.insert_child(root_child0, 0)

    root_child1 = yoga.Node(config)
    root_child1.set_height(10)
    root.insert_child(root_child1, 1)

    root_child2 = yoga.Node(config)
    root_child2.set_height(10)
    root.insert_child(root_child2, 2)
    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_LTR);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 100
    assert root_child0.get_computed_height() == 10

    assert root_child1.get_computed_left() == 0
    assert root_child1.get_computed_top() == 10
    assert root_child1.get_computed_width() == 100
    assert root_child1.get_computed_height() == 10

    assert root_child2.get_computed_left() == 0
    assert root_child2.get_computed_top() == 20
    assert root_child2.get_computed_width() == 100
    assert root_child2.get_computed_height() == 10

    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_RTL);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 100
    assert root_child0.get_computed_height() == 10

    assert root_child1.get_computed_left() == 0
    assert root_child1.get_computed_top() == 10
    assert root_child1.get_computed_width() == 100
    assert root_child1.get_computed_height() == 10

    assert root_child2.get_computed_left() == 0
    assert root_child2.get_computed_top() == 20
    assert root_child2.get_computed_width() == 100
    assert root_child2.get_computed_height() == 10


def test_flex_direction_row():
    config = yoga.Config()

    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_ABSOLUTE_PERCENTAGE_AGAINST_PADDING_EDGE, True)
    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_FIX_ABSOLUTE_TRAILING_COLUMN_MARGIN, True)

    root = yoga.Node(config)
    root.set_flex_direction(yoga.FLEX_DIRECTION_ROW)
    root.set_width(100)
    root.set_height(100)

    root_child0 = yoga.Node(config)
    root_child0.set_width(10)
    root.insert_child(root_child0, 0)

    root_child1 = yoga.Node(config)
    root_child1.set_width(10)
    root.insert_child(root_child1, 1)

    root_child2 = yoga.Node(config)
    root_child2.set_width(10)
    root.insert_child(root_child2, 2)
    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_LTR);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 10
    assert root_child0.get_computed_height() == 100

    assert root_child1.get_computed_left() == 10
    assert root_child1.get_computed_top() == 0
    assert root_child1.get_computed_width() == 10
    assert root_child1.get_computed_height() == 100

    assert root_child2.get_computed_left() == 20
    assert root_child2.get_computed_top() == 0
    assert root_child2.get_computed_width() == 10
    assert root_child2.get_computed_height() == 100

    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_RTL);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 90
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 10
    assert root_child0.get_computed_height() == 100

    assert root_child1.get_computed_left() == 80
    assert root_child1.get_computed_top() == 0
    assert root_child1.get_computed_width() == 10
    assert root_child1.get_computed_height() == 100

    assert root_child2.get_computed_left() == 70
    assert root_child2.get_computed_top() == 0
    assert root_child2.get_computed_width() == 10
    assert root_child2.get_computed_height() == 100


def test_flex_direction_column_reverse():
    config = yoga.Config()

    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_ABSOLUTE_PERCENTAGE_AGAINST_PADDING_EDGE, True)
    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_FIX_ABSOLUTE_TRAILING_COLUMN_MARGIN, True)

    root = yoga.Node(config)
    root.set_flex_direction(yoga.FLEX_DIRECTION_COLUMN_REVERSE)
    root.set_width(100)
    root.set_height(100)

    root_child0 = yoga.Node(config)
    root_child0.set_height(10)
    root.insert_child(root_child0, 0)

    root_child1 = yoga.Node(config)
    root_child1.set_height(10)
    root.insert_child(root_child1, 1)

    root_child2 = yoga.Node(config)
    root_child2.set_height(10)
    root.insert_child(root_child2, 2)
    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_LTR);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 90
    assert root_child0.get_computed_width() == 100
    assert root_child0.get_computed_height() == 10

    assert root_child1.get_computed_left() == 0
    assert root_child1.get_computed_top() == 80
    assert root_child1.get_computed_width() == 100
    assert root_child1.get_computed_height() == 10

    assert root_child2.get_computed_left() == 0
    assert root_child2.get_computed_top() == 70
    assert root_child2.get_computed_width() == 100
    assert root_child2.get_computed_height() == 10

    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_RTL);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 90
    assert root_child0.get_computed_width() == 100
    assert root_child0.get_computed_height() == 10

    assert root_child1.get_computed_left() == 0
    assert root_child1.get_computed_top() == 80
    assert root_child1.get_computed_width() == 100
    assert root_child1.get_computed_height() == 10

    assert root_child2.get_computed_left() == 0
    assert root_child2.get_computed_top() == 70
    assert root_child2.get_computed_width() == 100
    assert root_child2.get_computed_height() == 10


def test_flex_direction_row_reverse():
    config = yoga.Config()

    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_ABSOLUTE_PERCENTAGE_AGAINST_PADDING_EDGE, True)
    config.set_experimental_feature_enabled(yoga.EXPERIMENTAL_FEATURE_FIX_ABSOLUTE_TRAILING_COLUMN_MARGIN, True)

    root = yoga.Node(config)
    root.set_flex_direction(yoga.FLEX_DIRECTION_ROW_REVERSE)
    root.set_width(100)
    root.set_height(100)

    root_child0 = yoga.Node(config)
    root_child0.set_width(10)
    root.insert_child(root_child0, 0)

    root_child1 = yoga.Node(config)
    root_child1.set_width(10)
    root.insert_child(root_child1, 1)

    root_child2 = yoga.Node(config)
    root_child2.set_width(10)
    root.insert_child(root_child2, 2)
    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_LTR);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 90
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 10
    assert root_child0.get_computed_height() == 100

    assert root_child1.get_computed_left() == 80
    assert root_child1.get_computed_top() == 0
    assert root_child1.get_computed_width() == 10
    assert root_child1.get_computed_height() == 100

    assert root_child2.get_computed_left() == 70
    assert root_child2.get_computed_top() == 0
    assert root_child2.get_computed_width() == 10
    assert root_child2.get_computed_height() == 100

    root.calculate_layout(float("nan"), float("nan"), yoga.DIRECTION_RTL);

    assert root.get_computed_left() == 0
    assert root.get_computed_top() == 0
    assert root.get_computed_width() == 100
    assert root.get_computed_height() == 100

    assert root_child0.get_computed_left() == 0
    assert root_child0.get_computed_top() == 0
    assert root_child0.get_computed_width() == 10
    assert root_child0.get_computed_height() == 100

    assert root_child1.get_computed_left() == 10
    assert root_child1.get_computed_top() == 0
    assert root_child1.get_computed_width() == 10
    assert root_child1.get_computed_height() == 100

    assert root_child2.get_computed_left() == 20
    assert root_child2.get_computed_top() == 0
    assert root_child2.get_computed_width() == 10
    assert root_child2.get_computed_height() == 100
