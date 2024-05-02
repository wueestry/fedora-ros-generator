# Meta Package
Name:           ros-humble-iceoryx-binding-c
Version:        2.0.5
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://iceoryx.io
Summary:        Meta package for ros2-humble-iceoryx_binding_c and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-iceoryx_binding_c
Requires:       ros2-humble-iceoryx_binding_c-devel

Obsoletes: ros-humble-iceoryx-binding-c < 2.0.5-1

%description
Eclipse iceoryx inter-process-communication (IPC) middleware
C-Language Binding

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.5-1
- update to latest upstream
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.3-1
- update to latest upstream release
* Thu Jun 29 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.3-1
- update to latest upstream release
