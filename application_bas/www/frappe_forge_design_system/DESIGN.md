---
name: Frappe Forge Design System
colors:
  surface: '#f9f9ff'
  surface-dim: '#cadaff'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3ff'
  surface-container: '#e8edff'
  surface-container-high: '#e0e8ff'
  surface-container-highest: '#d7e2ff'
  on-surface: '#041b3c'
  on-surface-variant: '#434654'
  inverse-surface: '#1d3052'
  inverse-on-surface: '#edf0ff'
  outline: '#737685'
  outline-variant: '#c3c6d6'
  surface-tint: '#0c56d0'
  primary: '#003d9b'
  on-primary: '#ffffff'
  primary-container: '#0052cc'
  on-primary-container: '#c4d2ff'
  inverse-primary: '#b2c5ff'
  secondary: '#006a6a'
  on-secondary: '#ffffff'
  secondary-container: '#8cf3f3'
  on-secondary-container: '#007070'
  tertiary: '#414446'
  on-tertiary: '#ffffff'
  tertiary-container: '#595b5d'
  on-tertiary-container: '#d2d3d5'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#0040a2'
  secondary-fixed: '#8cf3f3'
  secondary-fixed-dim: '#6fd7d6'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#004f4f'
  tertiary-fixed: '#e1e2e4'
  tertiary-fixed-dim: '#c5c6c8'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9f9ff'
  on-background: '#041b3c'
  surface-variant: '#d7e2ff'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  code-md:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
  gutter: 1.5rem
  margin: 2rem
  max-width: 1280px
---

## Brand & Style

The brand personality is rooted in technical excellence, reliability, and precision. It targets a developer-centric audience that values efficiency and clarity over decorative flair. The emotional response should be one of "quiet confidence"—the UI feels robust enough to handle complex enterprise applications while remaining approachable and modern.

The design style follows a **Corporate / Modern** aesthetic with strong **Minimalist** influences. It prioritizes information density and structural integrity, utilizing a rigorous grid system and ample white space to prevent cognitive overload. The interface should feel like a high-performance tool: systematic, utilitarian, and impeccably organized.

## Colors

The palette is anchored by "Deep Atlantic" (Primary) and "Veridian Teal" (Secondary). The primary blue is used for high-priority actions and brand signifiers, while the teal serves as a secondary accent for success states or supplemental interactive elements. 

The background architecture relies on a "Slate Neutral" scale. Surfaces use pure white or very light grays to separate content sections, while text and iconography use a range of deep navy-grays to ensure high contrast and readability. Feedback colors (error, warning, success) should be slightly desaturated to maintain the professional, understated tone.

## Typography

This design system utilizes **Inter** exclusively for its systematic and utilitarian qualities. The typeface is optimized for screen readability at all sizes, particularly for technical documentation and data-heavy interfaces.

Headlines use tighter tracking and heavier weights to establish a clear hierarchy, while body text maintains a generous line height for long-form reading. Labels for metadata and small UI elements should use semi-bold weights or uppercase styling to distinguish them from standard body text. For code snippets or version numbers, a standard monospace fallback should be used to provide a technical "dev-centric" feel.

## Layout & Spacing

The design system employs a **Fixed Grid** model for desktop, centered within the viewport with a maximum width of 1280px. This ensures content remains legible on ultra-wide monitors. A 12-column grid system is used, allowing for flexible arrangements of application cards (3 or 4 per row) and sidebars.

The spacing rhythm follows a base-4 increment system to maintain mathematical consistency. Use "md" spacing for general padding within cards and containers, and "lg" spacing for separating major layout sections. Margin and gutter sizes are generous to reinforce the "plenty of white space" requirement.

## Elevation & Depth

Visual hierarchy is achieved through a combination of **Tonal Layers** and **Ambient Shadows**. 

1. **Base:** Background surfaces use a light gray (`#F4F5F7`) to provide a canvas.
2. **Surface:** Interactive containers like cards and sidebars use pure white.
3. **Shadows:** Use extremely soft, diffused shadows with a low opacity (4-8%) and a slight blue tint (`rgba(23, 43, 77, 0.08)`). This avoids the "muddy" look of pure black shadows and keeps the UI feeling clean.
4. **Active State:** On hover, shadows should increase in spread and blur slightly to simulate a "lift" effect, signaling interactivity.

## Shapes

The design system uses a "Rounded" (0.5rem) base corner radius. This strikes a balance between the clinical feel of sharp corners and the overly playful nature of pill shapes. 

- **Small Components:** Checkboxes and small tags use `rounded-sm` (4px).
- **Standard Components:** Buttons, input fields, and standard cards use the base `rounded-md` (8px).
- **Large Containers:** Modals and featured hero sections use `rounded-lg` (16px) to soften the large visual footprint.

## Components

### Buttons
Primary buttons use a solid Deep Blue fill with white text. Secondary buttons use a subtle gray stroke with primary-colored text. All buttons feature a 200ms transition on hover with a subtle background darkening.

### Cards
Cards are the primary vehicle for applications. They feature a white background, a 1px border (`#E1E4E8`), and the standard ambient shadow. Content inside cards should be strictly aligned to a internal padding of `1.5rem`.

### Input Fields
Inputs use a light gray border that transitions to the primary teal or blue on focus. Use placeholder text in a light neutral gray to maintain a clean appearance when empty.

### Chips & Tags
Use chips to denote application categories or status (e.g., "Stable", "Beta"). These should have low-saturation background tints of the primary/secondary colors with high-contrast text to remain readable but subordinate to the main title.

### Search & Filtering
Given the marketplace nature, the search bar should be prominent, featuring a subtle inner shadow to denote an "inset" look, distinguishing it from the "raised" application cards.