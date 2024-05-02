# Meta Package
Name:           ros-humble-urdfdom
Version:        3.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-urdfdom and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-urdfdom
Requires:       ros2-humble-urdfdom-devel

Obsoletes: ros-humble-urdfdom < 3.0.2-1

%description
A library to access URDFs using the DOM model.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- Initial humble build
