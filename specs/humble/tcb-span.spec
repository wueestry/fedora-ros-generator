# Meta Package
Name:           ros-humble-tcb-span
Version:        1.0.2
Release:        1%{?dist}
License:        Boost Software License
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-tcb_span and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tcb_span
Requires:       ros2-humble-tcb_span-devel

Obsoletes: ros-humble-tcb-span < 1.0.2-1

%description
Implementation of C++20's std::span

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest release
