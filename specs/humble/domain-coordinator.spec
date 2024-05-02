# Meta Package
Name:           ros-humble-domain-coordinator
Version:        0.10.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-domain_coordinator and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-domain_coordinator
Requires:       ros2-humble-domain_coordinator-devel

Obsoletes: ros-humble-domain-coordinator < 0.10.0-1

%description
A tool to coordinate unique ROS_DOMAIN_IDs across multiple processes

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- Initial humble build
