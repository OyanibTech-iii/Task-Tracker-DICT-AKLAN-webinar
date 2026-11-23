
---
name: python-modern-ios-ui
description: A comprehensive UI/UX design system for building premium, minimalist, iOS-inspired Python desktop applications using modern typography, consistent corner radii, Phosphor Icons, clean layouts, and solid colors.
---

# Python Modern iOS-Inspired UI/UX

## 1. Design Philosophy

Build modern, premium Python desktop applications inspired by Apple's iOS and macOS design language.

The interface must feel:
- Minimalist and sophisticated.
- Clean and visually balanced.
- Modern and premium.
- Intuitive and user-friendly.
- Consistent across all screens.
- Responsive and accessible.
- Functional without unnecessary decoration.

Adapt Apple's design principles to desktop applications rather than copying iOS interfaces literally.

Core principles:
- Less is more.
- Content comes first.
- Consistent spacing and alignment.
- Clear visual hierarchy.
- Generous whitespace.
- Subtle borders instead of excessive shadows.
- Rounded corners with consistent proportions.
- Restrained use of accent colors.

## 2. Strict Design Rules

These rules are mandatory.

| Element | Requirement |
|---|---|
| Gradients | STRICTLY PROHIBITED |
| Emojis | STRICTLY PROHIBITED |
| Icons | Phosphor Icons ONLY |
| Typography | Modern sans-serif |
| Buttons | Clean, rounded, minimal |
| Corner radius | Consistent throughout |
| Shadows | Subtle and restrained |
| Backgrounds | Solid colors only |
| Borders | Thin and subtle |
| Layout | Spacious and organized |
| Animations | Subtle and purposeful |

Never introduce:
- Gradient backgrounds or gradient buttons.
- Emoji-based icons.
- Excessive drop shadows.
- Excessive borders.
- Unnecessary decorative illustrations.
- Inconsistent button styles.
- Random corner radius values.
- Overly saturated colors.
- Unnecessary visual clutter.
- Mixed icon libraries.

## 3. Color System

Use a restrained color palette inspired by Apple's interface design.

### Light Theme

| Token | Color | Usage |
|---|---|---|
| Primary | #007AFF | Primary actions |
| Background | #F5F5F7 | Application background |
| Surface | #FFFFFF | Cards and panels |
| Text Primary | #1D1D1F | Main text |
| Text Secondary | #86868B | Supporting text |
| Border | #E5E5EA | Dividers and outlines |
| Success | #34C759 | Successful states |
| Warning | #FF9F0A | Warning states |
| Danger | #FF3B30 | Destructive actions |

### Dark Theme

| Token | Color | Usage |
|---|---|---|
| Primary | #0A84FF | Primary actions |
| Background | #000000 | Application background |
| Surface | #1C1C1E | Cards and panels |
| Text Primary | #FFFFFF | Main text |
| Text Secondary | #98989D | Supporting text |
| Border | #38383A | Dividers and outlines |
| Success | #30D158 | Successful states |
| Warning | #FFD60A | Warning states |
| Danger | #FF453A | Destructive actions |

### Color Guidelines

- Use solid colors only.
- Never use gradients.
- Avoid unnecessary accent colors.
- Maintain sufficient contrast.
- Use primary colors selectively.
- Use colors consistently across all screens.
- Support light and dark themes when appropriate.

## 4. Typography

Typography should resemble the clarity and readability of modern Apple interfaces.

### Preferred Fonts

1. SF Pro Display / SF Pro Text, where available and properly licensed.
2. Inter.
3. Segoe UI.
4. Arial as a fallback.

### Typography Scale

| Element | Font Size | Weight |
|---|---:|---|
| Large Page Title | 28–32px | Bold |
| Section Heading | 20–24px | Semibold |
| Card Heading | 16–18px | Semibold |
| Body Text | 14–16px | Regular |
| Supporting Text | 12–13px | Regular |
| Button Text | 14–15px | Semibold |
| Input Labels | 13–14px | Medium |

### Typography Rules

- Maintain a consistent font family.
- Use font weight to establish hierarchy.
- Avoid excessive font sizes.
- Avoid unnecessary uppercase text.
- Maintain comfortable line spacing.
- Use muted secondary text for descriptions.
- Never use decorative or handwritten fonts.

## 5. Corner Radius System

Rounded corners are essential to the visual identity.

| Component | Radius |
|---|---:|
| Small Buttons | 8px |
| Standard Buttons | 10px |
| Input Fields | 10px |
| Cards | 14px |
| Large Panels | 18px |
| Modal Dialogs | 20px |
| Floating Elements | 16px |
| Pills | 999px |

### Corner Radius Rules

- Avoid arbitrary radius values.
- Use larger radii for larger containers.
- Use smaller radii for compact controls.
- Use pill shapes only when appropriate.
- Maintain consistent rounding across related components.

## 6. Spacing and Layout

Use a consistent spacing system based on multiples of 4px.

| Token | Value |
|---|---:|
| XS | 4px |
| SM | 8px |
| MD | 12px |
| LG | 16px |
| XL | 24px |
| 2XL | 32px |
| 3XL | 48px |

### Layout Rules

- Maintain consistent page margins.
- Avoid overcrowded interfaces.
- Use whitespace to separate content.
- Align components to a common grid.
- Group related information.
- Keep navigation predictable.
- Ensure layouts adapt to different window sizes.

## 7. Button Design

Buttons must have a clean, modern iOS-inspired appearance.

### Primary Button

- Solid primary color background.
- White text.
- 10px corner radius.
- Height between 40px and 46px.
- Semibold typography.
- No gradients.
- No excessive shadows.

### Secondary Button

- Surface-colored background.
- Subtle border.
- Primary or dark text.
- Same height and radius as primary buttons.

### Tertiary Button

- Transparent background.
- No visible border.
- Minimal text treatment.
- Used for less important actions.

### Destructive Button

- Solid red background or restrained red text.
- Clearly communicate destructive actions.
- Use confirmation dialogs when appropriate.

### Button Interaction States

Every button must support:

- Default state.
- Hover state.
- Pressed state.
- Disabled state.
- Loading state, when applicable.

Interactions should be subtle and consistent. Avoid exaggerated scaling, bouncing, or flashy animations.

## 8. Input Fields and Forms

Form controls should be minimal, accessible, and easy to understand.

### Input Guidelines

- Consistent 40–46px control height.
- 10px corner radius.
- Subtle neutral border.
- Clear placeholder text.
- Visible focus state.
- Proper labels.
- Consistent internal padding.

### Form Behavior

- Validate inputs clearly.
- Display helpful error messages.
- Avoid unnecessary modal interruptions.
- Group related fields.
- Preserve entered values when validation fails.
- Use appropriate keyboard input types where available.

## 9. Cards and Containers

Cards should organize information without adding unnecessary visual weight.

### Card Guidelines

- White surface in light mode.
- Dark surface in dark mode.
- 14px corner radius.
- Subtle 1px border.
- Internal padding of 16–24px.
- Consistent spacing between cards.

Avoid excessive shadows and nested cards.

Use cards only when they improve information organization.

## 10. Iconography — Phosphor Icons ONLY

Phosphor Icons is the exclusive icon library.

Official resource:
https://phosphoricons.com/

Never use:
- Emojis.
- Unicode symbols as icons.
- Font Awesome.
- Bootstrap Icons.
- Material Icons.
- Lucide Icons.
- Random SVG icon collections.

### Recommended Icon Weights

- Regular: General interface icons.
- Light: Subtle minimalist interfaces.
- Bold: Important actions.
- Fill: Selected navigation items and active states.
- Duotone: Only when additional visual emphasis is genuinely necessary.

Prefer Regular and Fill for consistent interface design.

### Icon Guidelines

| Usage | Size |
|---|---:|
| Small Action Icons | 16px |
| Standard Interface Icons | 18–20px |
| Navigation Icons | 20–22px |
| Prominent Action Icons | 24px |

Maintain consistent stroke weight, proportions, and alignment.

### Suggested Icon Mapping

| Purpose | Phosphor Icon |
|---|---|
| Dashboard | SquaresFour |
| Settings | Gear |
| Search | MagnifyingGlass |
| Add | Plus |
| Edit | PencilSimple |
| Delete | Trash |
| User | User |
| Notifications | Bell |
| Home | House |
| Database | Database |
| Folder | Folder |
| Calendar | CalendarBlank |
| Analytics | ChartLine |
| Logout | SignOut |
| More Options | DotsThree |

Always verify icon names and availability in the installed Phosphor package.

## 11. Navigation Design

Navigation should be predictable and visually lightweight.

### Sidebar Navigation

- Solid background.
- No gradients.
- Consistent icon alignment.
- Clear active navigation state.
- Proper spacing between navigation items.
- Minimal separators.
- Consistent typography.

### Navigation Item States

Default:
- Neutral text.
- Neutral icon.
- Transparent background.

Active:
- Primary-colored icon.
- Primary-colored or high-contrast text.
- Subtle solid background.
- Rounded 8–10px container.

Hover:
- Subtle background change.
- No exaggerated animations.

## 12. Tables and Data Presentation

Tables should prioritize readability and information hierarchy.

- Use clean column headers.
- Maintain consistent row heights.
- Use subtle horizontal dividers.
- Avoid excessive vertical borders.
- Align numerical values appropriately.
- Provide clear empty states.
- Include search and filtering when useful.
- Use restrained status indicators.

Recommended row height: 44–52px.

Avoid unnecessary decorative table elements.

## 13. Modal Dialogs and Notifications

### Modal Dialogs

- Centered layout.
- Solid background.
- 18–20px corner radius.
- Clear title and description.
- Proper button hierarchy.
- Adequate internal padding.
- Avoid excessive width.

### Toast Notifications

Use minimal notifications with:

- Phosphor status icons.
- Short descriptive messages.
- Appropriate status colors.
- Consistent positioning.
- Subtle entrance and exit animations.

Never use emoji-based notifications.

## 14. Animation and Microinteractions

Animations should improve usability rather than distract users.

Recommended:
- 120–200ms hover transitions.
- 150–250ms modal transitions.
- Subtle opacity changes.
- Smooth navigation transitions.
- Small loading indicators.
- Clear interaction feedback.

Avoid:
- Bouncing interfaces.
- Excessive scaling.
- Flashing elements.
- Unnecessary parallax.
- Overly elaborate transitions.

Animations should respect reduced-motion preferences where possible.

## 15. Python Development Guidelines

Build maintainable and reusable UI components.

### Preferred Frameworks

Use the following framework priority:

1. PySide6 — preferred for polished, modern desktop applications.
2. PyQt6 — suitable alternative.
3. CustomTkinter — suitable for simpler desktop applications.
4. Tkinter — use when maintaining an existing application or when dependencies must remain minimal.

Do not replace an existing framework without a valid technical reason.

### Recommended Architecture

Separate application responsibilities:

```text
project/
├── main.py
├── ui/
│   ├── screens/
│   └── components/
├── styles/
│   ├── colors.py
│   ├── typography.py
│   └── theme.py
├── assets/
│   └── icons/
├── database/
│   ├── connection.py
│   └── queries.py
├── services/
├── models/
└── requirements.txt
```

### Code Quality

- Use reusable components.
- Avoid duplicated styling.
- Centralize design tokens.
- Separate business logic from presentation.
- Use meaningful variable and class names.
- Use type hints where practical.
- Handle exceptions properly.
- Avoid hardcoding colors and dimensions throughout the application.

### Theme Management

Create a centralized theme configuration.

Example:

```python
COLORS = {
    "primary": "#007AFF",
    "background": "#F5F5F7",
    "surface": "#FFFFFF",
    "text": "#1D1D1F",
    "secondary_text": "#86868B",
    "border": "#E5E5EA",
}

RADIUS = {
    "button": 10,
    "input": 10,
    "card": 14,
    "modal": 20,
}

SPACING = {
    "xs": 4,
    "sm": 8,
    "md": 12,
    "lg": 16,
    "xl": 24,
    "xxl": 32,
}
```

## 16. Responsive Design and Accessibility

- Support window resizing.
- Prevent clipped content.
- Maintain readable typography.
- Provide keyboard navigation.
- Use visible focus indicators.
- Provide accessible labels.
- Maintain sufficient color contrast.
- Never rely exclusively on color to communicate information.
- Ensure controls have appropriate minimum sizes.

## 17. Final UI Quality Checklist

### Visual Quality

- [ ] No gradients.
- [ ] No emojis.
- [ ] Phosphor Icons exclusively.
- [ ] Consistent typography.
- [ ] Consistent corner radius.
- [ ] Proper spacing.
- [ ] Clean visual hierarchy.
- [ ] No unnecessary decorations.
- [ ] Solid color backgrounds only.

### Components

- [ ] Buttons have all interaction states.
- [ ] Inputs have visible focus states.
- [ ] Cards use consistent styling.
- [ ] Modals have proper spacing.
- [ ] Tables are readable.
- [ ] Navigation is consistent.
- [ ] Light and dark themes are consistent.

### Development

- [ ] Reusable components.
- [ ] Centralized design tokens.
- [ ] Separated UI and business logic.
- [ ] No duplicated styling.
- [ ] Responsive layouts.
- [ ] Proper error handling.
- [ ] Maintainable project architecture.

## 18. Final Instruction

Whenever developing or modifying a Python application's interface, strictly follow this design system.

Do not introduce new visual styles without a clear design reason.

Prioritize usability, consistency, simplicity, and visual refinement.

The final result should feel like a carefully designed modern Apple-inspired desktop application, not a traditional Python utility window.

**Design Keywords:** Minimalist, Premium, Modern, Native-feeling, Clean, Consistent, Refined, Functional.
