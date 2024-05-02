# Meta Package
Name:           ros-humble-srdfdom
Version:        2.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/srdfdom
Summary:        Meta package for ros2-humble-srdfdom and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-srdfdom
Requires:       ros2-humble-srdfdom-devel

Obsoletes: ros-humble-srdfdom < 2.0.4-1

%description
Parser for Semantic Robot Description Format (SRDF).

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.4-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.4-1
- Initial humble build
