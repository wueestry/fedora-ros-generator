# Meta Package
Name:           ros-humble-interactive-markers
Version:        2.3.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-interactive_markers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-interactive_markers
Requires:       ros2-humble-interactive_markers-devel

Obsoletes: ros-humble-interactive-markers < 2.3.2-1

%description
3D interactive marker communication library for RViz and similar
tools.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.2-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.12.0-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.2-1
- Initial humble build
