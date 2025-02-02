from enum import EnumMeta

import pytest

from manim_slides.convert import (
    PDF,
    AutoAnimateEasing,
    AutoAnimateMatcher,
    AutoPlayMedia,
    AutoSlideMethod,
    BackgroundSize,
    BackgroundTransition,
    ControlsBackArrows,
    ControlsLayout,
    Converter,
    Display,
    JsBool,
    JsFalse,
    JsNull,
    JsTrue,
    KeyboardCondition,
    NavigationMode,
    PowerPoint,
    PreloadIframes,
    RevealJS,
    RevealTheme,
    ShowSlideNumber,
    SlideNumber,
    Transition,
    TransitionSpeed,
)


@pytest.mark.parametrize(
    ("enum_type",),
    [
        (JsTrue,),
        (JsFalse,),
        (JsBool,),
        (JsNull,),
        (ControlsLayout,),
        (ControlsBackArrows,),
        (SlideNumber,),
        (ShowSlideNumber,),
        (KeyboardCondition,),
        (NavigationMode,),
        (AutoPlayMedia,),
        (PreloadIframes,),
        (AutoAnimateMatcher,),
        (AutoAnimateEasing,),
        (AutoSlideMethod,),
        (Transition,),
        (TransitionSpeed,),
        (BackgroundSize,),
        (BackgroundTransition,),
        (Display,),
        (RevealTheme,),
    ],
)
def test_format_enum(enum_type: EnumMeta) -> None:
    for enum in enum_type:  # type: ignore[var-annotated]
        expected = str(enum)
        got = f"{enum}"

        assert expected == got

        got = "{enum}".format(enum=enum)

        assert expected == got

        got = format(enum, "")

        assert expected == got


@pytest.mark.parametrize(
    ("enum_type",),
    [
        (ControlsLayout,),
        (ControlsBackArrows,),
        (SlideNumber,),
        (ShowSlideNumber,),
        (KeyboardCondition,),
        (NavigationMode,),
        (AutoPlayMedia,),
        (PreloadIframes,),
        (AutoAnimateMatcher,),
        (AutoAnimateEasing,),
        (AutoSlideMethod,),
        (Transition,),
        (TransitionSpeed,),
        (BackgroundSize,),
        (BackgroundTransition,),
        (Display,),
    ],
)
def test_quoted_enum(enum_type: EnumMeta) -> None:
    for enum in enum_type:  # type: ignore[var-annotated]
        if enum in ["true", "false", "null"]:
            continue

        expected = "'" + enum.value + "'"
        got = str(enum)

        assert expected == got


@pytest.mark.parametrize(
    ("enum_type",),
    [
        (JsTrue,),
        (JsFalse,),
        (JsBool,),
        (JsNull,),
        (RevealTheme,),
    ],
)
def test_unquoted_enum(enum_type: EnumMeta) -> None:
    for enum in enum_type:  # type: ignore[var-annotated]
        expected = enum.value
        got = str(enum)

        assert expected == got


class TestConverter:
    @pytest.mark.parametrize(
        ("name", "converter"), [("html", RevealJS), ("pdf", PDF), ("pptx", PowerPoint)]
    )
    def test_from_string(self, name: str, converter: type) -> None:
        assert Converter.from_string(name) == converter
