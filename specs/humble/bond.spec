# Meta Package
Name:           ros-humble-bond
Version:        3.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/bond
Summary:        Meta package for ros2-humble-bond and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-bond
Requires:       ros2-humble-bond-devel

Obsoletes: ros-humble-bond < 3.0.2-1

%description
A bond allows two processes, A and B, to know when the other has
terminated, either cleanly or by crashing. The bond remains connected
until it is either broken explicitly or until a heartbeat times out.

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
* Mon Apr 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upsteam
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.8.6-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- Initial humble build
