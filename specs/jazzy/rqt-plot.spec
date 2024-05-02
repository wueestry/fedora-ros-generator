# Meta Package
Name:           ros-jazzy-rqt-plot
Version:        1.4.0
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_plot
Summary:        Meta package for ros2-jazzy-rqt_plot and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_plot
Requires:       ros2-jazzy-rqt_plot-devel

Obsoletes: ros-jazzy-rqt-plot < 1.4.0-1

%description
rqt_plot provides a GUI plugin visualizing numeric values in a 2D plot
using different plotting backends.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.4.0-1
- Update to latest release
