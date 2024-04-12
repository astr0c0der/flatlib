import os
import matplotlib.pyplot as plt
import numpy as np
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const

class DrawChart:

    def __init__(self, chart: Chart):
        self.chart = chart
        self.outer_radius = 1.32
        self.inner_radius = 1.2
        self.central_radius = 0.66
        self.central_inner_radius = 0.57
        self.fig, self.ax = self._setup_figure()

        self._draw_circles()
        self._draw_cusps()
        self._draw_signs()
        self._draw_planets()
        self._draw_house_cusp_degrees()
        self._draw_inner_circle_marks()
        self._draw_house_numbers()

    def _setup_figure(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.axis('equal')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        return fig, ax
    
    def dec2dms(self, longitude):
        zodiac_signs = [
            '\u2648', '\u2649', '\u264A', '\u264B',
            '\u264C', '\u264D', '\u264E', '\u264F',
            '\u2650', '\u2651', '\u2652', '\u2653'
        ]
        sign_num = int(longitude // 30)
        pos_in_sign = longitude - (sign_num * 30)
        deg = int(pos_in_sign)
        full_min = (pos_in_sign - deg) * 60
        minute = int(full_min)
        full_sec = round((full_min - minute) * 60)

        deg = "{:02d}".format(deg)
        minute = "{:02d}".format(minute)
        full_sec = "{:02d}".format(full_sec)

        return f"{deg}° {zodiac_signs[sign_num]} {minute}'{full_sec}"
    
    def normalize_angle(self, angle):
        """ Normalize the angle to be within the range [0, 360) degrees. """
        return angle % 360
    
    def _rotate_angle(self, angle):
        """Rotate angle so the Ascendant is on the left (180 degrees)."""
        ascendant = self.chart.get(const.ASC)
        ascendant_angle = np.deg2rad(ascendant.lon)
        return angle - ascendant_angle + np.pi  # Adjust to move Ascendant to 180 degrees (left side)

    def _draw_cusps(self):
    
        cusps_radians = [self._rotate_angle(np.deg2rad(self.chart.houses.get(cusp).lon)) for cusp in const.LIST_HOUSES]
        for cusp in cusps_radians:
            self.ax.plot([0, self.inner_radius * np.cos(cusp)], [0, self.inner_radius * np.sin(cusp)], color='black', lw=0.5)

        for cusp in cusps_radians:
            start_x, start_y = self.central_inner_radius * np.cos(cusps_radians), self.central_inner_radius * np.sin(cusps_radians)
            end_x, end_y = self.central_radius * np.cos(cusps_radians), self.central_radius * np.sin(cusps_radians)
            self.ax.plot([start_x, end_x], [start_y, end_y], color='black', lw=0.5, zorder=3)

    def _draw_circles(self):
        circles = [
            plt.Circle((0, 0), self.outer_radius, edgecolor='black', facecolor='none', linewidth=2),
            plt.Circle((0, 0), self.inner_radius, edgecolor='black', facecolor='none', linewidth=2),
            plt.Circle((0, 0), self.central_radius, edgecolor='black', facecolor='white', linewidth=1, zorder=3),
            plt.Circle((0, 0), self.central_inner_radius, edgecolor='black', facecolor='none', linewidth=1, zorder=3),
        ]
        for circle in circles:
            self.ax.add_artist(circle)

    def _draw_house_cusp_degrees(self):
        for cusp in const.LIST_HOUSES:
            house_obj = self.chart.houses.get(cusp)
            cusp_degree = house_obj.lon
            cusp_radian = np.deg2rad(cusp_degree)
            rotated_radian = self._rotate_angle(cusp_radian)  # Apply rotation based on Ascendant

            line_start_x = self.outer_radius * np.cos(rotated_radian)
            line_start_y = self.outer_radius * np.sin(rotated_radian)
            line_end_x = (self.outer_radius + 0.15) * np.cos(rotated_radian)
            line_end_y = (self.outer_radius + 0.15) * np.sin(rotated_radian)
            text_x = (self.outer_radius + 0.35) * np.cos(rotated_radian)
            text_y = (self.outer_radius + 0.35) * np.sin(rotated_radian)

            if house_obj.id == const.HOUSE1 or house_obj.id == const.HOUSE4 or house_obj.id == const.HOUSE7 or house_obj.id == const.HOUSE10:
                self.ax.plot([line_start_x, line_end_x], [line_start_y, line_end_y], color='black', lw=1)
                text_rotation = np.degrees(rotated_radian) if -np.pi/2 <= rotated_radian <= np.pi/2 else np.degrees(rotated_radian) + 180

                # Convert degrees to DMS format
                cusp_dms = self.dec2dms(cusp_degree)

                self.ax.text(text_x, text_y, f"{cusp_dms}",
                            horizontalalignment='center',
                            verticalalignment='center',
                            fontsize=10,
                            rotation=text_rotation,
                            rotation_mode='anchor')
            
    def _draw_signs(self):
        zodiac_signs = [
            '\u2648', '\u2649', '\u264A', '\u264B',
            '\u264C', '\u264D', '\u264E', '\u264F',
            '\u2650', '\u2651', '\u2652', '\u2653'
        ]
        angles = np.linspace(0, 2 * np.pi, len(zodiac_signs), endpoint=False)
        rotation_adjustment = np.deg2rad(15)  # Adjustment for placing labels nicely between lines

        # Pixel to coordinate ratio (assuming 1 unit = 400 pixels)
        pixel_to_coordinate = 1 / 400

        # Adjustments specifically for Sagittarius, Capricorn, Aquarius, and Pisces
        sign_adjustments = {
            '\u2650': 5 * pixel_to_coordinate,  # Sagittarius
            '\u2651': 5 * pixel_to_coordinate,  # Capricorn
            '\u2652': 4 * pixel_to_coordinate,  # Aquarius
            '\u2653': 4 * pixel_to_coordinate   # Pisces
        }

        # Rotate and draw lines for zodiac signs
        for angle in angles:
            rotated_angle = self._rotate_angle(angle)
            start_x, start_y = self.inner_radius * np.cos(rotated_angle), self.inner_radius * np.sin(rotated_angle)
            end_x, end_y = self.outer_radius * np.cos(rotated_angle), self.outer_radius * np.sin(rotated_angle)
            self.ax.plot([start_x, end_x], [start_y, end_y], color='black', lw=1)
            
            
        # Rotate and place zodiac sign symbols with adjustments
        for label, angle in zip(zodiac_signs, angles):
            adjusted_angle = self._rotate_angle(angle + rotation_adjustment)
            base_radius = (self.inner_radius + (self.outer_radius - self.inner_radius) / 2)
            adjustment_factor = sign_adjustments.get(label, 0)  # Get specific adjustment if exists, else 0
            adjusted_radius = base_radius - adjustment_factor  # Adjust inward by subtracting the adjustment_factor
            x, y = adjusted_radius * np.cos(adjusted_angle), adjusted_radius * np.sin(adjusted_angle)
            self.ax.text(x, y, label, horizontalalignment='center', verticalalignment='center',
                        fontsize=15, rotation=np.rad2deg(adjusted_angle) - 90)  # Adjust text rotation for readability

    def _draw_house_numbers(self):
        """
        Calculate cusps angles in degrees, determine rotation needed, normalize and rotate all cusp angles,
        close the loop by appending the first angle at the end, calculate midpoint angle, convert to radians for plotting,
        calculate the position for the house number text, calculate the house number, draw the house number.
        """
        # Calculate cusps angles in degrees
        cusps_angles = [self.chart.houses.get(cusp).lon for cusp in const.LIST_HOUSES]
        
        # Determine the rotation needed to bring the Ascendant to the left side (180 degrees)
        ascendant_angle = self.chart.get(const.ASC).lon
        rotation_needed = 180 - ascendant_angle
        
        # Normalize and rotate all cusp angles
        rotated_cusps = [self.normalize_angle(angle + rotation_needed) for angle in cusps_angles]
        
        # Make sure to close the loop by appending the first angle at the end
        rotated_cusps.append(rotated_cusps[0])

        text_radius = (self.central_radius + self.central_inner_radius) / 2

        for i in range(12):
            # Get the current and next cusp angle
            current_cusp = rotated_cusps[i]
            next_cusp = rotated_cusps[i + 1]

            # Calculate midpoint angle
            if next_cusp < current_cusp:
                # We have wrapped around, so we take the average and add 180, then normalize
                midpoint_angle = self.normalize_angle((current_cusp + next_cusp + 360) / 2)
            else:
                # The simple average is the midpoint
                midpoint_angle = (current_cusp + next_cusp) / 2

            # Convert to radians for plotting
            midpoint_radian = np.deg2rad(midpoint_angle)

            # Calculate the position for the house number text
            x = text_radius * np.cos(midpoint_radian)
            y = text_radius * np.sin(midpoint_radian)
            
            # House number calculation
            house_number = i + 1
            
            # Draw the house number
            self.ax.text(x, y, str(house_number), horizontalalignment='center', verticalalignment='center', fontsize=10, zorder=5)
    
    def _draw_planets(self):
        """
        Draw planets on a chart based on their positions, using specific planet glyphs. 
        Adjusts their positions to avoid overlap and applies rotation based on Ascendant. 
        The function does not take any parameters and does not return any value.
        """
        planet_glyphs = {
            const.SUN: '☉', const.MOON: '☽', const.MERCURY: '☿', const.VENUS: '♀',
            const.MARS: '♂', const.JUPITER: '♃', const.SATURN: '♄', const.URANUS: '♅',
            const.NEPTUNE: '♆', const.PLUTO: '♇', const.CHIRON: '⚷', const.NORTH_NODE: '☊',
            const.SOUTH_NODE: '☋', const.SYZYGY: '', const.PARS_FORTUNA: '⊗',
        }
        positions = []
        adjustment_factor = 0.9
        for planet in const.LIST_OBJECTS:
            planet_degree = self.chart.getObject(planet).lon
            planet_radian = np.deg2rad(planet_degree)
            rotated_radian = self._rotate_angle(planet_radian)  # Apply rotation based on Ascendant
            radius_adjusted = self.inner_radius * adjustment_factor
            x, y = radius_adjusted * np.cos(rotated_radian), radius_adjusted * np.sin(rotated_radian)
            x, y = self._adjust_position_for_overlap(x, y, positions)  # Adjust positions to avoid overlap
            positions.append((x, y))
            self.ax.text(x, y, planet_glyphs.get(planet, '?'),
                        horizontalalignment='center',
                        verticalalignment='center',
                        fontsize=17,
                        fontname='Symbola')

    def _adjust_position_for_overlap(self, x, y, positions, min_distance=0.09):
        """
        Adjusts the position to avoid overlap with existing positions.

        Parameters:
            x (float): x-coordinate of the position to adjust.
            y (float): y-coordinate of the position to adjust.
            positions (list): List of tuples representing existing positions.
            min_distance (float, optional): Minimum distance to maintain between positions. Defaults to 0.09.

        Returns:
            tuple: Adjusted x and y coordinates after avoiding overlap.
        """
        pixel_to_units = 1 / 400  # Conversion from pixels to coordinate system units
        extra_pixel_distance = pixel_to_units  # Distance of one extra pixel in units

        # Increase the min_distance by one pixel
        adjusted_min_distance = min_distance + extra_pixel_distance

        for px, py in positions:
            if (px - x)**2 + (py - y)**2 < adjusted_min_distance**2:
                dx, dy = -x, -y
                length = np.sqrt(dx**2 + dy**2)
                dx, dy = dx / length, dy / length
                x += dx * adjusted_min_distance
                y += dy * adjusted_min_distance
        return x, y

    def _draw_inner_circle_marks(self):
        """
        Draw inner circle marks on the plot based on certain conditions.
        """
        for i in range(360):
            angle = np.deg2rad(i)
            start_radius = self.inner_radius - 0.03 if i % 5 == 0 else self.inner_radius - 0.02
            start_x, start_y = start_radius * np.cos(angle), start_radius * np.sin(angle)
            end_x, end_y = self.inner_radius * np.cos(angle), self.inner_radius * np.sin(angle)
            self.ax.plot([start_x, end_x], [start_y, end_y], color='black', lw=1)

    def save_plot(self, filename, format='png', dpi=300, bbox_inches='tight', path=None):
        """
        Save the plot to a file with various customizable parameters.

        Parameters:
        - filename: name of the file to save the plot to, including extension
        - format: format of the file (e.g., 'png', 'jpg', 'svg', 'pdf', 'eps', 'tiff', 'ps')
        - dpi: dots per inch (resolution of the image)
        - bbox_inches: set to 'tight' to cut out extra whitespace around the plot or None to keep the default
        - path: directory path where the file will be saved (optional)
        """
        if path:
            full_filename = os.path.join(path, filename)
        else:
            full_filename = filename
        
        self.fig.savefig(full_filename, format=format, dpi=dpi, bbox_inches=bbox_inches)
        print(f"Plot saved as '{full_filename}' with resolution {dpi} DPI.")

    def show(self):
        self.ax.set_axis_off()
        plt.show()
geo = GeoPos('52n22', '6w27')
datetime = Datetime('1984/06/23', '07:51', '+02:00')
chart = Chart(datetime, geo, IDs=const.LIST_OBJECTS, hsys=const.HOUSES_PLACIDUS)
astro_chart = DrawChart(chart)
astro_chart.show()