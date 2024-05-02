# Meta Package
Name:           ros-iron-rqt-plot
Version:        1.2.3
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_plot
Summary:        Meta package for ros2-iron-rqt_plot and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_plot
Requires:       ros2-iron-rqt_plot-devel

Obsoletes: ros-iron-rqt-plot < 1.2.3-1

%description
rqt_plot provides a GUI plugin visualizing numeric values in a 2D plot
using different plotting backends.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.3-1
- Update to latest release
