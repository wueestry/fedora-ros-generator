# Meta Package
Name:           ros-humble-rqt-plot
Version:        1.1.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_plot
Summary:        Meta package for ros2-humble-rqt_plot and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_plot
Requires:       ros2-humble-rqt_plot-devel

Obsoletes: ros-humble-rqt-plot < 1.1.2-1

%description
rqt_plot provides a GUI plugin visualizing numeric values in a 2D plot
using different plotting backends.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.2-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.13-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.2-1
- Initial humble build
